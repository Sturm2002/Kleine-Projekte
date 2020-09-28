using System;

namespace GuessTheNum
{
    class Program
    {

        static void Main(string[] args)
        {
            var rand = new Random();

            while (1 == 1)
            {
                
                Console.WriteLine("From which number?");
                int Startnum = Convert.ToInt32(Console.ReadLine());

                Console.WriteLine("To which number?");
                int Endnum = Convert.ToInt32(Console.ReadLine());

                int randInt = rand.Next(Startnum, Endnum);
                int Guess = 0;

                while (1 == 1)
                {
                    Console.WriteLine("Guess The Number between " + Startnum + " and " + Endnum + " ! ");
                    
                    string input = Console.ReadLine();
                    int inputNum = Convert.ToInt32(input);

                    if (inputNum == randInt)
                    {
                        Console.WriteLine("Found! after : "+Guess+" tries");
                        break;

                    }

                    else
                    {
                        Console.WriteLine("Wrong!");
                        if (inputNum < randInt)
                        {
                            Console.WriteLine("Your number is to small!");
                        }
                        else
                        {
                            Console.WriteLine("Your number is to big!");
                        }
                        Guess++;
                    }

                }
                Console.Clear();
            }

        }
    }
}
// 58 Lines 28.09.2020
// Alex Bruksch
