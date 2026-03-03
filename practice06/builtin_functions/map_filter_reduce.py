from functools import reduce

def main():
    nums = [1, 2, 3, 4, 5, 6]

    # len, sum, min, max
    print("len:", len(nums))
    print("sum:", sum(nums))
    print("min:", min(nums))
    print("max:", max(nums))

    # map(): square
    sq = list(map(lambda x: x * x, nums))
    print("map square:", sq)

    # filter(): keep even
    evv = list(filter(lambda x: x % 2 == 0, nums))
    print("filter even:", evv)

    # reduce(): product
    prod = reduce(lambda a, b: a * b, nums, 1)
    print("reduce product:", prod)

    # sorted()
    mixed = [3, 1, 10, 2]
    print("sorted:", sorted(mixed))
    print("sorted desc:", sorted(mixed, reverse=True))

    # type conversion
    s = "123"
    print("int('123'):", int(s))
    print("float('3.14'):", float("3.14"))
    print("str(999):", str(999))
    print("list('abc'):", list("abc"))
    print("tuple([1,2]):", tuple([1, 2]))
    print("set([1,1,2]):", set([1, 1, 2]))

    # type checking
    print("isinstance(nums, list):", isinstance(nums, list))

if __name__ == "__main__":
    main()