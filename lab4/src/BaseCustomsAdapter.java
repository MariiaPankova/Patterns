import javax.management.ValueExp;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public abstract class BaseCustomsAdapter implements Customs{
    protected final float exchange_rate;
    protected final float tax_rate;
    protected static final Pattern regexPattern = Pattern.compile("(\\d+)USD");

    public BaseCustomsAdapter(float exchange_rate, float tax_rate) {
        this.exchange_rate = exchange_rate;
        this.tax_rate = tax_rate;

    }

    protected float vehiclePrice(String usdStr) {
        Matcher match =  regexPattern.matcher(usdStr.strip());
        if (match.matches()) {
            float usdFloat = Float.parseFloat(match.group(1));
            return usdFloat * exchange_rate;
        }
        else throw new IllegalArgumentException();
    }

    @Override
    public float tax(Auto auto) {
        return vehiclePrice(auto) * tax_rate;
    }
}
