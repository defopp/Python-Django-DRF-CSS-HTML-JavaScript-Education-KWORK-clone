from django.shortcuts import redirect


def if_login(func):
    def wrapper(*args, **kwargs) -> None:  
        print(args)      
        if args[1].user.is_authenticated:
            print('Реквест есть')
            result = func(*args,**kwargs)
            print('Обертка отработала')
            return result
        else: return redirect('login')
    return wrapper