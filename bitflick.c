/*
 * *** SOME TIPS ***
 * 1. Be sure to set the fuses of your ATTiny85.  I am using 8 MHz no clock dividing
 * -U lfuse:w:0xe2:m -U hfuse:w:0xdf:m -U efuse:w:0xff:m
 *
*/ 

#define _BV(bit) (1 << (bit))
/*
 * Using the macro gives a maximum refresh rate of 35.1 khz.
 * Hardcoding the direction and skipping the redundant register
 * settings increases the refresh rate to 39.2 khz. Since both
 * of these are sufficiently fast to avoid undesireable flicker,
 * I'll stick with the macro approach for the moment.
 * NOTE: Numbers above were obtained when chip was running at 1MHz.
 * Now running at 8 MHz and rates are 8x higher as expected.
*/
#define CPLEX(b1,b2,dir)     \
do {                          \
  DDRB = _BV(b1) | _BV(b2);   \
  if (dir) {PORTB = _BV(b1);} \
  else {PORTB = _BV(b2);}     \
}while(0)                     \

/* 
 * Defining labels for the LEDs.  Useful if the order of the
 * LEDS in the project is not the same as in the charlie-
 * plexing routine.
*/

#define L1 8
#define L2 4
#define L3 32
#define L4 16
#define L5 2
#define L6 1

/* 
 * Loop CPLEX, executing an LED lighting based on the lbit argument
 * Drops the refresh rate to 21.3 khz.
*/
void cplexloop(int lbit, int stop, int duty)
{
  int t, c=0;
  t = millis();
  if(c++%100<duty)
  do {
    if( (1<<0) & lbit ) CPLEX(PB0,PB1,1);
    if( (1<<1) & lbit ) CPLEX(PB0,PB1,0);
    if( (1<<2) & lbit ) CPLEX(PB0,PB3,1);
    if( (1<<3) & lbit ) CPLEX(PB0,PB3,0);
    if( (1<<4) & lbit ) CPLEX(PB1,PB3,1);
    if( (1<<5) & lbit ) CPLEX(PB1,PB3,0);
  }while (millis()-t < stop);
}
int i;
void setup()
{
  //MCUCR |= _BV(PUD);
 
}
void loop()
{
  
  /*
  CPLEX(PB0,PB1,1);
  CPLEX(PB0,PB1,0);
  CPLEX(PB0,PB3,1);
  CPLEX(PB0,PB3,0);
  CPLEX(PB1,PB3,1);
  CPLEX(PB1,PB3,0);
  */
  cplexloop(42, 1000, 50);
  cplexloop(21, 1000, 100);
} 

/* *** CODE CAVE ***

*** Original hardcoding of registers and bits to Charlieplex 6 LEDs with 3 GPIO pins
  // 01-0
  DDRB = _BV(PB0)|_BV(PB1);
  PORTB = _BV(PB0);
  // 01-1
  //DDRB = _BV(PB0)|_BV(PB1);
  PORTB = _BV(PB1);
  // 03-0
  DDRB = _BV(PB0)|_BV(PB3);
  PORTB = _BV(PB0);
  // 03-3
  //DDRB = _BV(PB0)|_BV(PB3);
  PORTB = _BV(PB3);
  // 13-1
  DDRB = _BV(PB1)|_BV(PB3);
  PORTB = _BV(PB1);
  // 13-3
  //DDRB = _BV(PB1)|_BV(PB3);
  PORTB = _BV(PB3);

*/

