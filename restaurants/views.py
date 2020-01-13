from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {"my_list":
    	[
    		{"restaurant_name":"Burger king","food_type":"Fast food"},
    		{"restaurant_name":"Pizza Hot","food_type":"Pizza"},
    		{"restaurant_name":"Baza","food_type":"Kuwait food"}
    	],

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {"my_object":
    	{"restaurant_name":"Baza","food_type":"Kuwait food"}
    }
    return render(request, 'detail.html', context)
