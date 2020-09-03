from django.shortcuts import render
from rest_framework import status, viewsets
from .serializer import EmpdetailsSerializer, CustomerDetailsSerializer
from .models import Empdetails, CustomerDetails

from rest_framework.views import APIView
from rest_framework.response import Response
import os
from django.conf import settings

class CustomerDetailsView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to create/update/view customer.
    """
    queryset = CustomerDetails.objects.all()
    serializer_class = CustomerDetailsSerializer
    def create(self, request, *args, **kwargs):
        """
            Create a list of model instances if a list is provides or a
            single model instance otherwise.
        """
        data = request.data
        if isinstance(data, list):
            serializer = self.get_serializer(data=request.data, many=True)
        else:
            serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED,
                    headers=headers)


# Create your views here.

class EmpdetailsView(viewsets.ModelViewSet):
    """
    API endpoint that allows users to create/update/view customer.
    """
    queryset = Empdetails.objects.all()
    serializer_class = EmpdetailsSerializer

class EmpdashboardView(APIView):
    def get(self, request):
        dashboard_details = {};
        emp_details = Empdetails.objects.all();
        serializer = EmpdetailsSerializer(emp_details, many=True);
        dashboard_details["emp_count"] = len(serializer.data);
        dashboard_details["grade_count"] = {};
        dashboard_details["subgrade_count"] = {};
        dashboard_details["skills_count"] = {};
        for dic in serializer.data:
            if dic['grade'] in dashboard_details["grade_count"]:
                dashboard_details["grade_count"][dic['grade']].append(dic['grade']);
            else:
                dashboard_details["grade_count"][dic['grade']] = [dic['grade']];
            if dic['sub_grade'] in dashboard_details["subgrade_count"]:
                dashboard_details["subgrade_count"][dic['sub_grade']].append(dic['sub_grade']);
            else:
                dashboard_details["subgrade_count"][dic['sub_grade']] = [dic['sub_grade']];
            for skl in dic['skills'].split(','):
                if skl in dashboard_details["skills_count"]:
                    dashboard_details["skills_count"][skl].append(skl);
                else:
                    dashboard_details["skills_count"][skl] = [skl];
        print(dashboard_details)
        return Response({"dashboard_details": dashboard_details});

from django.shortcuts import render
import openpyxl


def fileUpload(request):
    if "GET" == request.method:
        return render(request, 'test_app/index.html', {})
    else:
        excel_file = request.FILES["excel_file"]

        # you may put validations here to check extension or file size

        wb = openpyxl.load_workbook(excel_file)

        # getting a particular sheet by name out of many sheets
        worksheet = wb["Sheet1"]
        print(worksheet)

        excel_data = list()
        # iterating over the rows and
        # getting value from each cell in row
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)

        return render(request, 'test_app/index.html', {"excel_data":excel_data})

class ListUsers(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        # usernames = [user.username for user in User.objects.all()]
        
        import pandas as pd
        file_name = os.path.join(settings.BASE_DIR, 'template.xlsx');
        df = pd.read_excel(file_name)
        df = df.fillna(method='ffill')
        file_data = df.to_dict(orient='record');
        for key,value in enumerate(file_data):
            value['Over all Skills'] = value['Over all Skills'].split(',');
            file_data[key] = value;
        return Response(file_data);