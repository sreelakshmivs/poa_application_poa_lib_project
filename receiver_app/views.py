import jwt
from django.http import JsonResponse
from django.shortcuts import render
from pathlib import Path
from poalib_srevat import poadecode

pub_key = Path('receiver_app/public_key.pem').read_text()

def receive_jwt(request):
    jwt_token = request.headers.get('Authorization', '').replace('Bearer ', '')
    print(f"Received JWT token: {jwt_token}")


    try:
        #decoded_token = jwt.decode(jwt_token, pub_key, algorithms=["HS256"])
        decoded_token = poadecode.decode_and_validate_poa("eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJwcmluY2lwYWwgcHVibGljIGtleSI6InByaW5jaXBhbCBwdWJpYyBrZXkiLCJhdWQiOiJkZmRkLWZkZmRmZC1kZmRmLWRmIiwibWV0YWRhdGEiOiJhZ2VudCBuYW1lOnh4LCBwcmluY2lwYWwgbmFtZTp4eCwgYWdlbnQgTUFDIElEOnh4LCBhcHBsaWNhdGlvbiB0eXBlOnh4IiwicmVzb3VyY2Ugb3duZXIgaWQiOiJmZ2ZnZi1mZy1mZyIsInRyYW5zZmVyYWJsZSI6IjAiLCJjcmVkZW50aWFscyI6IlNlbmQgUG9BIHRvIHJlc291cmNlIG93bmVyIGlkIiwiaWF0IjoxNjkyMTA0NjkxLCJleHAiOjE2OTIxOTEwOTEuOTQ3NzgzfQ.Ek1PqUdgZjlC-EYBm24heRqW6uxlVlLhkD9p4cMBk1c0bhKnmDX5ORJGMfopzIm04JzNBYK3FrEhaxPrwrya0nmcf5L5j3T4OY_XYVRO--2iv-gs5yF6cOzI7QOXjdXwcD8_kl4LemOi5ii2Vqiz2T2mHcHmyEiVoRjP9QcxuhGhcyZ6dhBICurZQu4U3xxR3zY22ng_f0RM36D2eMXyWHHSblaJHVQ4iO6N_dKVmjxWeyovrY28qcblgc5hEazI5aRkyQBAhTCTttyikFO2qrP4PtCAq6kvnV3qoQXq905XkvCboXQovJ-Rt0D9RW9AtsUzT94_A-U6BtuSb3-zjA",
                                                          pub_key, "dfdd-fdfdfd-dfdf-df")
        ###In the above line, you can give jwt_token parameter or copy paste actual token in full length, but the first option don't work :)
        print("Decoded token:", decoded_token)
        return JsonResponse(decoded_token)
    except jwt.ExpiredSignatureError:
        return JsonResponse({"error": "JWT token has expired"})
    except jwt.DecodeError:
        return JsonResponse({"error": "Invalid JWT token"})

def receiver_template_view(request):
    print("MADDDDDDDDDD")
    return render(request, 'receiver_app/receiver_template.html')