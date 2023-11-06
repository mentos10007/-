const
int
rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 2;
LiquidCrystal
lcd(rs, en, d4, d5, d6, d7);
int x = 0;

void setup()
{

lcd.begin(20, 4);
}


void loop()
{


lcd.setCursor(x, 0);
lcd.print("hi");
delay(1000);
x = x + 1;
lcd.clear();

if (x == 19) x = 0;

}
