import urllib.request
import urllib.parse


class WebBrowser:


    def __init__(self):

        self.name = "Internet Tool"



    def search(self, query):

        encoded = urllib.parse.quote(
            query
        )


        url = (
            "https://www.google.com/search?q="
            + encoded
        )


        return (
            "Search link created:\n"
            + url
        )



    def open_url(self, url):

        try:

            response = urllib.request.urlopen(
                url,
                timeout=10
            )


            data = response.read()


            return data.decode(
                "utf-8",
                errors="ignore"
            )


        except Exception as error:

            return (
                f"Internet error: {error}"
            )
