public interface Builder {
    Builder reset();
    Pizza getResult();
    Builder chooseDough(Dough dough);
    Builder addIngredient(Pizza.Filling filling, int num);
}



