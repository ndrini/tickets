from scrapy.http import FormRequest
#!/usr/bin/python
from yaml import safe_load

with open(r'secrets.yaml') as data_file:
    data = safe_load(data_file)
    assert type(data) == dict
    lang_list = [i for i in data] 

    print(data['user'])
    print(data['password'])
    


# with open(r'settings.yaml') as data_file:
#     data = safe_load(data_file)
#     assert type(data) == dict
#     lang_list = [i for i in data] 



# Now instead of using start_url at the start of our spiders we use a start_requests() method. This allows us to use methods related to form filling.
# Lets look underneath the hood of the scrapy.spider code to see how this works. Remember this is where we always refer to when starting a spider.
# When we call the start_requests() method from that class this is what is under the hood.

# def start_requests(self):
#     for url in self.start_urls:
#          yield self.make_requests_from_url(url)
         
# def make_requests_from_url(self, url): 
#     return Request(url, dont_filter=True)


# # def start_requests(self):
# #    return [
# #       FormRequest("INSERT URL", formdata={"user":"user",   
# #            "pass":"pass"}, callback=self.parse)]
           
# # def parse(self,response):
# #     pass

