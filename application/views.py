import tempfile
import os
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .transcriber import transcribe_audio_file


@csrf_exempt
@require_POST
def transcribe_view(request):
    if 'audio_file' not in request.FILES:
        return JsonResponse({'error': 'No audio file provided.'}, status=400)

    audio_file = request.FILES['audio_file']

    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            for chunk in audio_file.chunks():
                temp_audio.write(chunk)
            temp_path = temp_audio.name

        try:
            transcribed_text = transcribe_audio_file(temp_path)
            print(transcribed_text)
            return JsonResponse({'transcription': transcribed_text})
        finally:
            os.unlink(temp_path)

    except RuntimeError as e:
        return JsonResponse({'error': str(e)}, status=503)
    except Exception as e:
        return JsonResponse({'error': f'An unexpected error occurred: {str(e)}'}, status=500)