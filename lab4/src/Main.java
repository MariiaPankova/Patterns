public class Main {
    public static void main(String[] args) {
        Auto truck = new Auto(10, "Car1", true, 335);
        Auto car = new Auto(3, "Car2", false, 1000);
        CarCustomsAdapter carCustomsAdapter = new CarCustomsAdapter(29.55f, 0.10f);
        TruckCustomsAdapter truckCustomsAdapter = new TruckCustomsAdapter(29.55f, 0.10f);
        System.out.println("Car price: " + carCustomsAdapter.vehiclePrice(car) + " tax: " + carCustomsAdapter.tax(car));
        System.out.println("Truck price: " + truckCustomsAdapter.vehiclePrice(truck) + " tax: " + truckCustomsAdapter.tax(truck));
    }
}
