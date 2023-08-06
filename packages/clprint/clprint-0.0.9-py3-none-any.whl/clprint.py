from core.decorator import clprint_colors, clprint_highlighters

# Functions for coloring the output of the console - General Use


def __label_print_fuc(label):
    print(f"[{label}]   :", end=' ')


@clprint_colors['red'].decorate
def print_r(ctx,  *args, label=None, **kwargs):
    '''Prints the content in red'''
    if label:
        __label_print_fuc(label)
    print(ctx, *args, **kwargs)


@clprint_colors['green'].decorate
def print_g(ctx,  *args, label=None, **kwargs):
    '''Prints the content in green'''
    if label:
        __label_print_fuc(label)
    print(ctx, *args, **kwargs)


@clprint_colors['blue'].decorate
def print_b(ctx,  *args, label=None, **kwargs):
    '''Prints the content in blue'''
    if label:
        __label_print_fuc(label)
    print(ctx, *args, **kwargs)


@clprint_colors['yellow'].decorate
def print_y(ctx,  *args, label=None, **kwargs):
    '''Prints the content in yellow'''
    if label:
        __label_print_fuc(label)
    print(ctx, *args, **kwargs)


@clprint_colors['purple'].decorate
def print_p(ctx,  *args, label=None, **kwargs):
    '''Prints the content in purple'''
    if label:
        __label_print_fuc(label)
    print(ctx, *args, **kwargs)


# Functions for coloring the output of the console - Highlighting
@clprint_highlighters['red'].decorate
def print_rh(ctx,  *args, label=None, **kwargs):
    '''Prints the content red with seperator'''
    if label:
        __label_print_fuc(label)
    print(ctx, *args, **kwargs)


@clprint_highlighters['green'].decorate
def print_gh(ctx,  *args, label=None, **kwargs):
    '''Prints the content green with seperator'''
    if label:
        __label_print_fuc(label)
    print(ctx, *args, **kwargs)


@clprint_highlighters['blue'].decorate
def print_bh(ctx,  *args, label=None, **kwargs):
    '''Highlights the content in blue with seperator'''
    if label:
        __label_print_fuc(label)
    print(ctx, *args, **kwargs)


@clprint_highlighters['yellow'].decorate
def print_yh(ctx,  *args, label=None, **kwargs):
    '''Highlights the content in yellow with seperator'''
    if label:
        __label_print_fuc(label)
    print(ctx, *args, **kwargs)


@clprint_highlighters['purple'].decorate
def print_ph(ctx,  *args, label=None, **kwargs):
    '''Highlights the content in purple with seperator'''
    if label:
        __label_print_fuc(label)
    print(ctx, *args, **kwargs)
