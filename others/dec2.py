def p_decorate(func):
   def func_wrapper(name):
       f = func(name)
       return "<p>" + f +"</p>"
   return func_wrapper


def strong_decorate(func):
    def func_wrapper(name):
        f = func(name)
        return "<strong>"+ f + "</strong>"
    return func_wrapper


def div_decorate(func):
    def func_wrapper(name):
        f1 = func(name)
        return "<div>"+ f1 +"</div>"
    return func_wrapper


@div_decorate
@p_decorate
@strong_decorate
def get_text(name):
    return "lorem ipsum, "+ name + "dolor sit amet"

print get_text("John")
