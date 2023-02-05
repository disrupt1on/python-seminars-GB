import view
import process
import log

def button_click():
    mode = str(view.inp_mode())
    if mode == 'импорт' or mode == 'Импорт':
        surname = view.inp_import()
        result_search = process.search(surname)
        view.view_import(result_search)
        log.log_cash(mode, surname)
    elif mode == 'экспорт' or mode == 'Экспорт':
        result = view.inp_export()
        process.export(result)
        log.log_cash(mode, result[1::])