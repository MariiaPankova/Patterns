import com.vehiclecalculator.CarCalculator;

public class CarCustomsAdapter extends BaseCustomsAdapter {
    public CarCustomsAdapter(float exchange_rate, float tax_rate) {
        super(exchange_rate, tax_rate);
    }

    @Override
    public float vehiclePrice(Auto auto) {
        CarCalculator carCalculator = new CarCalculator(auto.model, auto.age, auto.damaged ? 0 : 1);
        return vehiclePrice(carCalculator.calculatePrice());
    }
}
