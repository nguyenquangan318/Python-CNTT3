from tabulate import tabulate

def display_records(atendances):
    table = []
    for atend in atendances:
        atend_list = [atend['id'], atend['name'], atend['times'][0], atend['times'][1] if atend['times'][1] else '[Đang làm việc]']
        table.append(atend_list)
    print('--- BẢNG CHẤM CÔNG ---')
    print(tabulate(table, tablefmt="github"))