//*2.2.1. Ось вже й закінчився карантин, що стримував розвиток ресторанного бізнесу.
// Іванко, вирішує відкрити свою власну справу і вирішує почати з невеликої кав’ярні,
// у ТРЦ Мех-мат Мол. Початково у кав’ярні він запланував готувати такі чотири напої:
// Еспресо, Американо, Капучіно та Латте. Кожен з цих напоїв має собівартість,
// що складається з сумарної вартості компонент, що входять до напою та вартість
// продажу цього напою клієнту. Допоможіть Іванкові у цій не легкій справі.
// Змоделюйте роботу цієї кав’ярні, реалізувавши Реалізуйте шаблон Фабричний
// метод та порахуйте прибуток, який отримає ця кав’ярня за певний проміжок часу.
// Розширте асортимент напоїв у кав’ярні іншими напоями.*//


import java.util.Scanner;

public class Main {
        public static void main(String[] args) {
            Drink drink;
            Cafe espressomaker = new CafeEspresso();
            Cafe americanomaker = new CafeAmericano();
            Cafe lattemaker = new CafeLatte();
            Cafe cappuccinomaker = new CafeCappuccino();
            Cafe teamaker = new CafeTea();
            int daily_income = 0;
            Scanner in = new Scanner(System.in);


            String order = in.nextLine();
            while (!order.equals("0")){
                switch (order.toLowerCase()){
                    case "espresso":
                        drink = espressomaker.make_coffee();
                        daily_income = daily_income +  drink.sell();
                        System.out.println("That will be " + drink.sell_cost + " please");
                        order = in.nextLine();

                    case "americano":
                        drink = americanomaker.make_coffee();
                        daily_income = daily_income +  drink.sell();
                        System.out.println("That will be " + drink.sell_cost + " please");
                        order = in.nextLine();

                    case "latte":
                        drink = lattemaker.make_coffee();
                        daily_income = daily_income +  drink.sell();
                        System.out.println("That will be " + drink.sell_cost + " please");
                        order = in.nextLine();

                    case "cappuccino":
                        drink = cappuccinomaker.make_coffee();
                        daily_income = daily_income +  drink.sell();
                        System.out.println("That will be " + drink.sell_cost + " please");
                        order = in.nextLine();

                    case "tea":
                        drink = teamaker.make_coffee();
                        daily_income = daily_income +  drink.sell();
                        System.out.println("That will be " + drink.sell_cost + " please");
                        order = in.nextLine();
                }
            }
            System.out.println("No more orders, your income is " +daily_income);

        }
    }
