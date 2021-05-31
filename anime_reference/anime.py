from typing import Optional, List
try:
    from anime_reference.Naruto import Naruto
    from anime_reference.constants import *
except:
    from Naruto import Naruto
    from constants import *

def get_summary(title: str, episode_name: str) -> Optional[str]:
    """
    Description: Gets the summary of a given anime episode.

        Parameters:
        -----------
        title (str): anime title
        epsisode_name (str): anime episode name

        Returns:
        --------
        str: summary of anime episode
    """
    title_lower = title.lower()
    anime = anime_object(title_lower)
    try:
        return anime.episode_summary(episode_name)
    except AttributeError:
        return None

def get_episode_names(title: str) -> Optional[List[str]]:
    """
    Description: Gets all episode names of a given anime title.

        Parameters:
        -----------
        title (str): anime title

        Returns:
        --------
        List[str]: List of all anime episode names
    """
    title_lower = title.lower()
    anime = anime_object(title_lower)
    try:
        return anime.episode_names
    except AttributeError:
        return None
    
def get_episodes(title: str) -> Optional[int]:
    """
    Description: Gets the number of episodes for a given anime title.

        Parameters:
        -----------
        title (str): anime title

        Returns:
        --------
        int: Number of episodes
    """
    title = title.lower()
    anime = anime_object(title)
    try:
        return anime.episodes
    except AttributeError:
        return None

def get_movie_names(title: str) -> Optional[List[str]]:
    """
    Description: Gets all episode names of a given anime title.

        Parameters:
        -----------
        title (str): anime title

        Returns:
        --------
        List[str]: List of all anime movie names
    """
    return None

def get_movies(title: str) -> Optional[int]:
    """
    Description: Gets the number of movies for a given anime title.

        Parameters:
        -----------
        title (str): anime title

        Returns:
        --------
        int: Number of movies
    """
    return None

def get_synopsis(title: str) -> Optional[str]:
    """
    Description: Gets a complete synopsis of a given anime title.

        Parameters:
        -----------
        title (str): anime title
        
        Returns:
        --------
        str: A complete synopsis of a given anime title
    """
    return None

def get_anime_titles() -> Optional[List[str]]:
    """
    Description: Gets all anime titles currently supported.

        Parameters:
        -----------
        None
        
        Returns:
        --------
        List[str]: List of all anime titles currently supported
    """
    return None

def anime_object(title: str):
    """
    Description: Converts the anime title into the correct
                 anime-reference anime object

        Parameters:
        -----------
        title (str): anime title
        
        Returns:
        --------
        Optional[]: List of all anime titles currently supported
    """
    if title in NARUTO.keys():
        return Naruto(title)
    else:
        print(f"Title {title} is not a valid title.")
        return None
    
if __name__ == "__main__":
    print(get_summary("naruto shippuden", "Naruto and Hinata"))
