from supabase import Client, create_client
import os


class SupabaseDB:
    """
    class instance for database connection to supabase

    :str: url: configuration for database url for data inside supafast project
    :str: key: configuration for database secret key for authentication
    :object: supabase: Supabase instance for connection to database environment
    """

    url: str = os.getenv('PROJECT_URL')
    key: str = os.getenv('API_KEY')
    supabase: Client = create_client(url, key)
