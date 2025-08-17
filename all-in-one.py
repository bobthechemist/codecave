'''
Combines all files in a project directory into one markdown file.  
I find this a useful way to pull a project together into one document for submitting to a LLM for Agentic refactoring and such.
'''
import os
import re
import sys

from collections import defaultdict

def get_gitignore_patterns(gitignore_path):
    """Reads and parses a .gitignore file."""
    patterns = []
    if os.path.exists(gitignore_path):
        with open(gitignore_path, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    # Convert gitignore pattern to regex
                    regex_pattern = line.replace('.', r'\.').replace('*', '.*')
                    patterns.append(re.compile(regex_pattern))
    return patterns

def is_ignored(path, gitignore_patterns):
    """Checks if a file or directory should be ignored."""
    for pattern in gitignore_patterns:
        if pattern.search(path):
            return True
    return False

def get_language_from_extension(file_extension):
    """Maps file extensions to markdown language identifiers."""
    extension_map = {
        '.py': 'python',
        '.js': 'javascript',
        '.html': 'html',
        '.css': 'css',
        '.java': 'java',
        '.c': 'c',
        '.cpp': 'cpp',
        '.cs': 'csharp',
        '.rb': 'ruby',
        '.php': 'php',
        '.swift': 'swift',
        '.kt': 'kotlin',
        '.go': 'go',
        '.rs': 'rust',
        '.ts': 'typescript',
        '.json': 'json',
        '.xml': 'xml',
        '.yml': 'yaml',
        '.yaml': 'yaml',
        '.md': 'markdown',
        '.sh': 'shell',
        '.sql': 'sql',
    }
    return extension_map.get(file_extension.lower(), '')

def combine_files_to_markdown(project_dir, output_file='all-in-one.md'):
    """
    Combines all text files in a project directory into a single markdown file,
    respecting .gitignore, with proper directory headings and syntax highlighting.
    """
    gitignore_path = os.path.join(project_dir, '.gitignore')
    gitignore_patterns = get_gitignore_patterns(gitignore_path)
    
    project_files = defaultdict(list)

    for root, dirs, files in os.walk(project_dir, topdown=True):
        # Exclude .git directory
        if '.git' in dirs:
            dirs.remove('.git')

        # Filter ignored directories
        dirs[:] = [d for d in dirs if not is_ignored(os.path.join(root, d), gitignore_patterns)]
        
        for file in files:
            file_path = os.path.join(root, file)
            if not is_ignored(file_path, gitignore_patterns) and file != output_file:
                relative_dir = os.path.relpath(root, project_dir)
                project_files[relative_dir].append(file)
                
    with open(output_file, 'w') as outfile:
        for directory in sorted(project_files.keys()):
            outfile.write(f"## {directory}\n\n")
            for file in sorted(project_files[directory]):
                file_path = os.path.join(project_dir, directory, file)
                _, file_extension = os.path.splitext(file)
                language = get_language_from_extension(file_extension)
                
                outfile.write(f"### {file}\n\n")
                outfile.write(f"```{language}\n")

                try:
                    with open(file_path, 'r', errors='ignore') as infile:
                        outfile.write(infile.read())
                except Exception as e:
                    outfile.write(f"Error reading file: {e}")

                outfile.write("\n```\n\n")

if __name__ == "__main__":
    # Check if a command-line argument for the directory is provided
    if len(sys.argv) > 1:
        project_directory = sys.argv[1]
    else:
        # Default to the current working directory if no argument is given
        project_directory = os.getcwd()

    # Verify that the provided path is a valid directory
    if not os.path.isdir(project_directory):
        print(f"Error: The specified path '{project_directory}' is not a valid directory.")
        sys.exit(1)

    # Define the output file path within the target directory
    output_file_path = os.path.join(project_directory, 'all-in-one.md')

    print(f"Processing directory: {project_directory}")
    combine_files_to_markdown(project_directory, output_file_path)
    print(f"Successfully created 'all-in-one.md' in {project_directory}")
