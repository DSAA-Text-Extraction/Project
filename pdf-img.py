import cloudconvert

def cloud_convert(page_range,path):
	api = cloudconvert.Api('jJihZWVlAY2YoYnSmSOvHIADAt8BXI0G6jwb1DLKzJKIVIodL7qqWrMXoQ8SVDBy')
	process = api.convert({
    	'inputformat': 'pdf',
    	'outputformat': 'jpg',
    	'converteroptions': {
        	'page_range': page_range#'7-10'
    	},
    	'input': 'upload',
    	'file': open(path, 'rb')
	})
	process.wait() 
	process.download("/home/username/dsaa-project/images")

cloud_convert('9-10', '/home/username/dsaa-project/pdfs/sol.pdf')
