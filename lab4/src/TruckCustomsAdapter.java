import com.vehiclecalculator.CarCalculator;
import com.vehiclecalculator.TruckCalculator;

public class TruckCustomsAdapter extends BaseCustomsAdapter {
    public TruckCustomsAdapter(float exchange_rate, float tax_rate) {
        super(exchange_rate, tax_rate);
    }

    @Override
    public float vehiclePrice(Auto auto) {
        TruckCalculator truckCalculator = new TruckCalculator(auto.age, auto.mileage);
        return vehiclePrice(truckCalculator.calculatePrice());
    }
}
