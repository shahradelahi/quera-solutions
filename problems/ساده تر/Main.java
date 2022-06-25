import java.math.RoundingMode;
import java.text.DecimalFormat;
import java.util.Scanner;

public class Main {

    static Scanner sc;
    public static void main(String[] args) {
        sc = new Scanner(System.in);

        float Numbers[] = new float[4];
        Numbers[0] = sc.nextInt();
        Numbers[1] = sc.nextInt();
        Numbers[2] = sc.nextInt();
        Numbers[3] = sc.nextInt();

        float Sum = Numbers[0] + Numbers[1] + Numbers[2] + Numbers[3];

        float Average;
        if(Sum == 0)
            Average = Sum - Sum;
        else
            Average = Sum / 4;
        float Product = Numbers[0] * Numbers[1] * Numbers[2] * Numbers[3];
        float MAX = Math.max(Numbers[0], Math.max(Numbers[1], Math.max(Numbers[2], Numbers[3])));
        float MIN = Math.min(Numbers[0], Math.min(Numbers[1], Math.min(Numbers[2], Numbers[3])));

        DecimalFormat df = new DecimalFormat("#.000000");
        df.setRoundingMode(RoundingMode.CEILING);

        if(Sum == 0)
            System.out.println("Sum : 0.000000");
        else
            System.out.println("Sum : " + df.format(Sum));

        if(Average == 0)
            System.out.println("Average : 0.000000");
        else
            System.out.println("Average : " + df.format(Average));

        if(Product == 0)
            System.out.println("Product : 0.000000");
        else
            System.out.println("Product : " + df.format(Product));

        if(MAX == 0)
            System.out.println("MAX : 0.000000");
        else
            System.out.println("MAX : " + df.format(MAX));

        if(MIN == 0)
            System.out.println("MIN : 0.000000");
        else
            System.out.println("MIN : " + df.format(MIN));
    }
}