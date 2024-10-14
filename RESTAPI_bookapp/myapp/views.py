from django.shortcuts import render
import requests


# Create your views here.
def index(request):
	if request.method=='POST':
		action=request.POST.get('action')
		if action=='add':
			url='http://localhost:8001/books'
			querystring={'title':request.POST['title'],'isbn':request.POST['isbn'],'publisher':request.POST['publisher'],'author':request.POST['author']}
			response=requests.post(url,json=querystring)
			print(response)
			msg='Data Inserted successfully'
			return render(request,'index.html',{'msg':msg})
			

		if action=='select':
			isbn=request.POST.get('isbn')
			
			try:
				url = f'http://localhost:8001/books/{isbn}'
				print(f"API URL: {url}")
				response = requests.get(url)
				if response.status_code == 200:
					book_data = response.json()
					print(f"Book Data: {book_data}")
					msg = 'Book Found'
					return render(request, 'index.html', {
		                'msg': msg,
		                'title': book_data.get('title', 'Unknown Title'),  # Fallback to 'Unknown Title'
		                'isbn': book_data.get('isbn', 'Unknown ISBN'),      # Fallback to 'Unknown ISBN'
		                'publisher': book_data.get('publisher', 'Unknown Publisher'),  # Fallback to 'Unknown Publisher'
		                'author': book_data.get('author', 'Unknown Author')  # Fallback to 'Unknown Author'
		            })
				elif response.status_code == 404:
					msg = 'Book Not Found'
					return render(request, 'index.html', {'msg': msg})
				else:
					msg = 'An error occurred while fetching book data'
					return render(request, 'index.html', {'msg': msg})
			except:
				msg='Book Not Found'
				return render(request,'index.html',{'msg':msg})

		if action=='update':
			isbn=request.POST.get('isbn')
			
			try:
				url = f'http://localhost:8001/books/{isbn}'
				querystring={'title':request.POST['title'],'isbn':request.POST['isbn'],'publisher':request.POST['publisher'],'author':request.POST['author']}
				response=requests.put(url, json=querystring)
				msg='Data Updated successfully'
				return render(request, 'index.html', {'msg': msg })
			except:
				msg='Book Not Found'
				return render(request,'index.html',{'msg':msg})

		if action=='delete':
			isbn=request.POST.get('isbn')
			
			try:
				url = f'http://localhost:8001/books/{isbn}'
				response=requests.delete(url)
				msg='Book deleted successfully'
				return render(request, 'index.html', {'msg': msg}) 
			except:
				msg='Book Not Found'
				return render(request,'index.html',{'msg':msg})

			
		else:
			msg='Invalid Action'
			return render(request,'index.html',{'msg':msg})
	else:
		return render(request,'index.html')
