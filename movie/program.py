import movie_svc
import requests.exceptions

def main():
    show_header()
    search_event_loop()


def show_header():
    print('-----------------------------')
    print('      MOVIE SEARCH APP')
    print('-----------------------------')
    print()


def search_event_loop():
    search = "ONCE_THROUGH_LOOP"

    while search != 'x':
        try:
            search = input("Movie to search (x to exit): ")
            if search != 'x':
                results = movie_svc.search_movies(search)
                print(f"Found {len(results)} results.")
                for r in results:
                    print(f"{r.year} -- {r.title.strip()}")
                print()
        except requests.exceptions.ConnectionError:
            print(f"Error: Your network is down.")
        except ValueError:
            print(f"Error: Search text is required.")
        except Exception as x:
            print(f"Unexpected error. Details: {type(x)}")

    print("Exiting...")



if __name__ == "__main__":
    main()