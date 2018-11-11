package com.shuva.tyrestats;

/*
-- In my last long drive, the odometer did not match either Google maps or my manual mileage calculation.
-- It occurred to me that this may be due to worn-out tyres. The car odometer is tuned by the number of wheel rotations.
-- So, if my tyres are worn out, then the circumference is less.
-- This means that the car would think it travelled more for every rotation than it actually did.
-- Car odometer reading says 517kms travel and 18.8 kmpl mileage --> There is error margin here.
-- Manual calculation from tank full to tank full consumed 29.24 litres of fuel. Google maps distance = 510kms. --> Assume this is correct.
-- Car tyres are 7 years old worn out.
-- Can I find how much did the car tyre wear out?
 */
public class TyreStats {
    private static final double odometerDistance = 517;
    private static final double actualDistance = 510;
    private static final int TyreWidth = 195;
    private static final int aspectRatio = 55;
    private static final int tyreDiameter = 16;

    public static void main(String args[]) {
        //My tyre profile is  195/55R16

        double radius = GetTyreRadius(TyreWidth,aspectRatio,tyreDiameter);
        double circumference = GetCircumference(radius);
        System.out.println("Radius = " + radius + " mm");
        System.out.println("Circumference = " + circumference + " mm");

        System.out.println("Each rotation of wheel moves " + circumference + " mm . This is what the car thinks");
        double rotations = odometerDistance*1000*1000/circumference;
        System.out.println("In 521kms odometer travel, tyre rotated " +  rotations + " times");

        System.out.println("But the tyres were worn out and effective circumference was less. So the distance actually travelled would be less.");
        System.out.println("As per Google maps, the distance travelled is " + actualDistance + " kms.");
        System.out.println("There is a difference of " + (odometerDistance - actualDistance) + " kms");

        System.out.println("How much did the tyre wear out?");

        //Rotations * wornOutCirm = actualDistance kms)
        double wornOutcircum = (actualDistance*1000*1000/rotations);
        System.out.println("Worn our circum = " + wornOutcircum + " mm");
        double wornOutRadius = wornOutcircum/(2*(22/7));
        System.out.println("Worn our radius = " + wornOutRadius + " mm");
        System.out.println("===========================");
        System.out.println("Rubber worn out = " + (radius - wornOutRadius + " mm"));
        System.out.println("===========================");
    }

    private static double GetCircumference(double radius) {
        return 2* (22/7) * radius;
    }

    /*
    Example: 195/55R16  (width, aspectRation, diameter
     */
    static double GetTyreRadius(int width, int aspectRatio, int diameter) {
        //Since diameter is in inch. Convert to mm.
        double diameterInMm = (diameter/0.39370)*10;
        double rubberHeightFromRim = (aspectRatio*width)/100;
        return (diameterInMm + 2*rubberHeightFromRim)/2;
    }
}

