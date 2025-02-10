import shutil
import time


def format_time(seconds):
    """
    This function return a string with the time in the format MM:SS
    """
    m, s = divmod(seconds, 60)
    return f"{int(m):02d}:{int(s):02d}"


def ft_tqdm(lst: range) -> None:
    """
    Mimics the tqdm function :
    displays a progress bar and some information about the iteration

    the percentage of the iteration
    the progress bar
    the current iteration and the total
    the time passed since the beginning of the iteration and the time left
    the speed of the iteration

    yield makes ft_tqdm a generator, meaning values are produced one at a time
    instead of all at once.
    """
    total = len(lst)
    width_bar = shutil.get_terminal_size().columns - 40
    start_time = time.time()

    for i, item in enumerate(lst, start=1):

        info_percent = i / total * 100
        percent = int(i / total * width_bar)
        progress_bar = f"|{'█' * percent:<{width_bar}}|"

        range_time = f"{i}/{total}"

        time_passed = time.time() - start_time
        speed = i / time_passed if time_passed > 0 else 0
        time_left = (total - i) / speed if speed > 0 else 0

        time_passed_formated = format_time(time_passed)
        time_left_formated = format_time(time_left)

        time_info = f"[{time_passed_formated}<{time_left_formated}, \
            {speed:.2f}it/s]"

        print(f"\r{info_percent:.0f}%{progress_bar} \
              {range_time} {time_info}", end="\r")
        yield item


def main():
    for _ in ft_tqdm(range(333)):
        pass


if __name__ == "__main__":
    main()
