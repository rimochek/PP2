def main():
    names = ["Alice", "Bob", "Charlie"]
    ages = [19, 22, 18]

    # enumerate()
    print("=== enumerate ===")
    for i, name in enumerate(names, start=1):
        print(i, name)

    # zip()
    print("=== zip ===")
    for name, age in zip(names, ages):
        print(name, "->", age)

    # zip to dict
    d = dict(zip(names, ages))
    print("dict from zip:", d)

    # zip with different lengths (cuts to shortest)
    extra = [100, 200]
    print("zip different lengths:", list(zip(names, extra)))

if __name__ == "__main__":
    main()