from prototype import ClonableStringBuilder

if __name__ == '__main__':
    builder = ClonableStringBuilder()
    builder.append_substring("My fauvorite ")\
           .append_substring("drink is ")
    builder_2 = builder.clone()

    builder.append_substring("coffee")
    builder_2.append_substring("tee")

    print(builder.get_result())
    print(builder_2.get_result())