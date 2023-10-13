from rest_framework.views import APIView
from rest_framework.response import Response
from .mnist_model import predict
import numpy as np
import logging


logger = logging.getLogger(__name__)

from rest_framework.views import APIView
from rest_framework.response import Response
from .mnist_model import predict
import numpy as np
import logging


class PredictDigit(APIView):
    def post(self, request, format=None):
        try:
            image_data = request.FILES.get("image")
            if not image_data:
                return Response(
                    {"error": "Aucune image n'a été téléchargée."}, status=400
                )

            prediction = predict(image_data)
            print(prediction)

            response_headers = {
                "X-Custom-Header": "Valeur personnalisée",
            }

            return Response({"prediction": prediction}, headers=response_headers)

        except Exception as e:
            logger.error(str(e))
            return Response({"error": str(e)}, status=500)
