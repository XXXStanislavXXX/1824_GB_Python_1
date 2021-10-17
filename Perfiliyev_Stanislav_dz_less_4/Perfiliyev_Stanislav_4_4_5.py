from cbr_parser import extract_date, currency_rates


def ref_cur_rates(argv: str):
    module, arg = argv
    cur_cost, cur_date = currency_rates(arg)
    return cur_cost, cur_date


if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        cur_cost, cur_date = ref_cur_rates(sys.argv)
    else:
        cur_cost = None
        cur_date = extract_date()
    exit(print(cur_cost, cur_date, sep=', '))
