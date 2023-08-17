import jwt
from django.http import JsonResponse
from django.shortcuts import render  # Import the render function
from datetime import datetime, timedelta
from poalib_srevat import poalib
from pathlib import Path

private_key_pem = Path('sender_app/private_key.pem').read_text()

def send_jwt(request):
    now = datetime.utcnow()
    payload = {
        'principal public key': "principal pubic key",
        'aud': "dfdd-fdfdfd-dfdf-df",
        'metadata': "agent name:xx, principal name:xx, agent MAC ID:xx, application type:xx",
        'resource owner id': "fgfgf-fg-fg",
        'transferable': "0",
        'credentials': "Send PoA to resource owner id",
        'iat': now,
        'exp': (now + timedelta(hours=24)).timestamp(),
    }

    #jwt_token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
    jwt_token = poalib.generate_poa(private_key_pem, payload)
    jwt_token_str = jwt_token
    return JsonResponse({"message": "JWT sent successfully", "jwt_token": jwt_token_str})

def sender_template_view(request):
    return render(request, 'sender_app/sender_template.html')
