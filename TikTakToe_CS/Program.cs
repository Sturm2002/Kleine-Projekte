using System;
using System.Collections;
using System.Collections.Generic;
using System.Threading;

namespace TikTakToe
{
    class Program
    {
        static void Main(string[] args)
        {
            var rand = new Random();
            ArrayList Playfield = new ArrayList();
            bool running = true;
            while (true)
            {
                Playfield.Clear();

            Playfield.Add(" ");
            Playfield.Add(" ");
            Playfield.Add(" ");

            Playfield.Add(" ");
            Playfield.Add(" ");
            Playfield.Add(" ");

            Playfield.Add(" ");
            Playfield.Add(" ");
            Playfield.Add(" ");
                running = true;
                while (running == true)
                {

                    Console.Clear();
                    Console.WriteLine(" \n {0} | {1} | {2}\n---+---+---\n {3} | {4} | {5}\n---+---+---\n {6} | {7} | {8}", Playfield[0], Playfield[1], Playfield[2], Playfield[3], Playfield[4], Playfield[5], Playfield[6], Playfield[7], Playfield[8]);

                    bool ValidInp = false;
                    while (ValidInp != true)
                    {
                        string input = Console.ReadLine();
                        switch (input)
                        {
                            case "11":
                                if (Convert.ToString(Playfield[0]) == " ")
                                {
                                    Playfield[0] = "X";
                                    ValidInp = true;
                                }
                                else
                                {
                                    Console.WriteLine("Wrong Input!");
                                }
                                break;

                            case "12":
                                if (Convert.ToString(Playfield[1]) == " ")
                                {
                                    Playfield[1] = "X";
                                    ValidInp = true;
                                }
                                else
                                {
                                    Console.WriteLine("Wrong Input!");
                                }
                                break;

                            case "13":
                                if (Convert.ToString(Playfield[2]) == " ")
                                {
                                    Playfield[2] = "X";
                                    ValidInp = true;
                                }
                                else
                                {
                                    Console.WriteLine("Wrong Input!");
                                }
                                break;

                            case "21":
                                if (Convert.ToString(Playfield[3]) == " ")
                                {
                                    Playfield[3] = "X";
                                    ValidInp = true;
                                }
                                else
                                {
                                    Console.WriteLine("Wrong Input!");
                                }
                                break;

                            case "22":
                                if (Convert.ToString(Playfield[4]) == " ")
                                {
                                    Playfield[4] = "X";
                                    ValidInp = true;
                                }
                                else
                                {
                                    Console.WriteLine("Wrong Input!");
                                }
                                break;

                            case "23":
                                if (Convert.ToString(Playfield[5]) == " ")
                                {
                                    Playfield[5] = "X";
                                    ValidInp = true;
                                }
                                else
                                {
                                    Console.WriteLine("Wrong Input!");
                                }
                                break;

                            case "31":
                                if (Convert.ToString(Playfield[6]) == " ")
                                {
                                    Playfield[6] = "X";
                                    ValidInp = true;
                                }
                                else
                                {
                                    Console.WriteLine("Wrong Input!");
                                }
                                break;

                            case "32":
                                if (Convert.ToString(Playfield[7]) == " ")
                                {
                                    Playfield[7] = "X";
                                    ValidInp = true;
                                }
                                else
                                {
                                    Console.WriteLine("Wrong Input!");
                                }
                                break;

                            case "33":
                                if (Convert.ToString(Playfield[8]) == " ")
                                {
                                    Playfield[8] = "X";
                                    ValidInp = true;
                                }
                                else
                                {
                                    Console.WriteLine("Wrong Input!");
                                }
                                break;

                            default:
                                Console.Clear();
                                Console.WriteLine(" \n {0} | {1} | {2}\n---+---+---\n {3} | {4} | {5}\n---+---+---\n {6} | {7} | {8}", Playfield[0], Playfield[1], Playfield[2], Playfield[3], Playfield[4], Playfield[5], Playfield[6], Playfield[7], Playfield[8]);

                                Console.WriteLine("Wrong Input!");
                                break;

                        }

                    }
                    Console.Clear();
                    Console.WriteLine(" \n {0} | {1} | {2}\n---+---+---\n {3} | {4} | {5}\n---+---+---\n {6} | {7} | {8}", Playfield[0], Playfield[1], Playfield[2], Playfield[3], Playfield[4], Playfield[5], Playfield[6], Playfield[7], Playfield[8]);

                    bool freeRand = false;
                    while (freeRand == false)
                    {
                        int BotInp = rand.Next(0, 8);
                        if (Convert.ToString(Playfield[BotInp]) == " ")
                        {
                            freeRand = true;
                            Playfield[BotInp] = "O";
                        }
                    }
                    Thread.Sleep(1000);


                    if (Playfield[0] == Playfield[1] && Playfield[1] == Playfield[2])
                    {
                        if (Convert.ToString(Playfield[0]) == "X")
                        {
                            Console.WriteLine("You've Won!");
                            running = false;
                            Thread.Sleep(2000);
                        }
                        else if (Convert.ToString(Playfield[0]) == "O")
                        {
                            Console.WriteLine("You've Lost!");
                            running = false;
                            Thread.Sleep(2000);
                        }

                    }
                    else if (Playfield[3] == Playfield[4] && Playfield[4] == Playfield[5])
                    {
                        if (Convert.ToString(Playfield[3]) == "X")
                        {
                            Console.WriteLine("You've Won!");
                            running = false;
                            Thread.Sleep(2000);
                        }
                        else if (Convert.ToString(Playfield[3]) == "O")
                        {
                            Console.WriteLine("You've Lost!");
                            running = false;
                            Thread.Sleep(2000);
                        }
                    }
                    else if (Playfield[6] == Playfield[7] && Playfield[7] == Playfield[8])
                    {
                        if (Convert.ToString(Playfield[6]) == "X")
                        {
                            Console.WriteLine("You've Won!");
                            running = false;
                            Thread.Sleep(2000);
                        }
                        else if (Convert.ToString(Playfield[6]) == "O")
                        {
                            Console.WriteLine("You've Lost!");
                            running = false;
                            Thread.Sleep(2000);
                        }
                    }
                    else if (Playfield[0] == Playfield[3] && Playfield[3] == Playfield[6])
                    {
                        if (Convert.ToString(Playfield[0]) == "X")
                        {
                            Console.WriteLine("You've Won!");
                            running = false;
                            Thread.Sleep(2000);
                        }
                        else if (Convert.ToString(Playfield[0]) == "O")
                        {
                            Console.WriteLine("You've Lost!");
                            running = false;
                            Thread.Sleep(2000);
                        }
                    }
                    else if (Playfield[1] == Playfield[4] && Playfield[4] == Playfield[7])
                    {
                        if (Convert.ToString(Playfield[1]) == "X")
                        {
                            Console.WriteLine("You've Won!");
                            running = false;
                            Thread.Sleep(2000);
                        }
                        else if (Convert.ToString(Playfield[1]) == "O")
                        {
                            Console.WriteLine("You've Lost!");
                            running = false;
                            Thread.Sleep(2000);
                        }
                    }
                    else if (Playfield[2] == Playfield[5] && Playfield[5] == Playfield[8])
                    {
                        if (Convert.ToString(Playfield[2]) == "X")
                        {
                            Console.WriteLine("You've Won!");
                            running = false;
                            Thread.Sleep(2000);
                        }
                        else if (Convert.ToString(Playfield[2]) == "O")
                        {
                            Console.WriteLine("You've Lost!");
                            running = false;
                            Thread.Sleep(2000);
                        }
                    }
                    else if (Playfield[0] == Playfield[4] && Playfield[4] == Playfield[8])
                    {
                        if (Convert.ToString(Playfield[0]) == "X")
                        {
                            Console.WriteLine("You've Won!");
                            running = false;
                            Thread.Sleep(2000);
                        }
                        else if (Convert.ToString(Playfield[0]) == "O")
                        {
                            Console.WriteLine("You've Lost!");
                            running = false;
                            Thread.Sleep(2000);
                        }
                    }
                    else if (Playfield[2] == Playfield[4] && Playfield[4] == Playfield[6])
                    {
                        if (Convert.ToString(Playfield[2]) == "X")
                        {
                            Console.WriteLine("You've Won!");
                            running = false;
                            Thread.Sleep(2000);
                        }
                        else if (Convert.ToString(Playfield[2]) == "O")
                        {
                            Console.WriteLine("You've Lost!");
                            running = false;
                            Thread.Sleep(2000);
                        }
                    }
                }
            }
        }
    }
}
