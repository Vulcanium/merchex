from django.shortcuts import render, redirect
from django.core.mail import send_mail

from listings.forms import ContactUsForm, BandForm, ListingForm
from listings.models import Band, Listing


def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/band_list.html", {"bands": bands})


def band_detail(request, band_id):
    band = Band.objects.get(id = band_id)
    return render(request, "listings/band_detail.html", {"band": band})


def band_create(request):

    if request.method == 'POST':
        # Create an instance of our form and populate it with the POST data
        form = BandForm(request.POST)

        if form.is_valid():
            # Create a new "Band", save it to the database, and redirects to the detail page of the band we just created
            band = form.save()
            return redirect("band-detail", band.id)
        
        # If the form is not valid, we let the execution continue down to the return below and display the form again (with errors)

    else:
        # This must be a GET request, so create an empty form
        form = BandForm()

    return render(request, "listings/band_create.html", {"form" : form})


def listing_list(request):
    listings = Listing.objects.all()
    return render(request, "listings/listing_list.html", {"listings": listings})


def listing_detail(request, listing_id):
    listing = Listing.objects.get(id = listing_id)
    return render(request, "listings/listing_detail.html", {"listing": listing})


def listing_create(request):
    
    if request.method == 'POST':
        # Create an instance of our form and populate it with the POST data
        form = ListingForm(request.POST)

        if form.is_valid():
            # Create a new "Listing", save it to the database, and redirects to the detail page of the listing we just created
            listing = form.save()
            return redirect("listing-detail", listing.id)
        
        # If the form is not valid, we let the execution continue down to the return below and display the form again (with errors)

    else:
        # This must be a GET request, so create an empty form
        form = ListingForm()
    

    return render(request, "listings/listing_create.html", {"form" : form})


def contact(request):

    if request.method == "POST":
        # Create an instance of our form and populate it with the POST data
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(
                subject = f"Message from {form.cleaned_data["name"] or "anonymous"} via MerchEx Contact Us form",
                message = form.cleaned_data["message"],
                from_email = form.cleaned_data["email"],
                recipient_list = ["admin@merchex.xyz"],
            )

            return redirect("email-sent")

        # If the form is not valid, we let the execution continue down to the return below and display the form again (with errors)

    else:
        # This must be a GET request, so create an empty form
        form = ContactUsForm()
    
    return render(request, "listings/contact.html", {"form" : form})


def email_sent(request):
    return render(request, "listings/email_sent.html")


def about(request):
    return render(request, "listings/about.html")