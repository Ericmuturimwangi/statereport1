from django.shortcuts import render
from .models import HQ, Brigade, Unit, PDFSubmission, BrigadeReport
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import PDFSubmissionSerializer, BrigadeReportSerializer, UnitSerializer, BrigadeSerializer


class PDFSubmissionViewSet(viewsets.ModelViewSet):
    queryset = PDFSubmission.objects.all()
    serializer_class = PDFSubmissionSerializer

    @action(detail=True, methods=['post'])
    def send_to_brigade(self, request, pk=None):
        submission = self.get_object()
        if submission.status != PDFSubmission.SubmissionStatus.PENDING:
            return Response({"detail": "Submission is not pending."}, status=status.HTTP_400_BAD_REQUEST)
        
        submission.status = PDFSubmission.SubmissionStatus.IN_BRIGADE
        submission.save()
        return Response({"detail": "Submission sent to Brigade"}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['post'])
    def send_to_hq(self, request, pk=None):
        submission = self.get_object()
        if submission.status !=PDFSubmission.SubmissionStatus.IN_BRIGADE:
            return Response ({"detail": "SUbmission is not in the Brigade,"}, status=status.HTTP_400_BAD_REQUEST)
        
        submission.status = PDFSubmission.SubmissionStatus.IN_HQ
        submission.save()
        return Response({"detail": "Submission sent to HQ"}, status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['post'])
    def complete_submission(self, request, pk=None):
        submission = self.get_object()
        if submission.status != PDFSubmission.SubmissionStatus.IN_HQ:
            return Response({"detail": "Submission is not in HQ."}, status=status.HTTP_400_BAD_REQUEST)
        
        submission.status = PDFSubmission.SubmissionStatus.COMPLETED
        submission.save()
        return Response({"detail": "Submission completed."}, status=status.HTTP_200_OK)
    
class BrigadeReportViewSet(viewsets.ModelViewSet):
    queryset = BrigadeReport.objects.all()
    serializer_class = BrigadeReportSerializer

    @action(detail=True, methods=['post'])
    def compile_report(self, request, pk=None):
        brigade = self.get_object()
        submissions = PDFSubmission.objects.filter(unit__brigade=brigade, status=PDFSubmission.SubmissionStatus.IN_HQ)
        # pdfgeneration
        compiled_pdf = self.compile_pdf(submissions)

        # save
        report = BrigadeReport.objects.create(
            brigade=brigade,
            compiled_file=compiled_pdf,
            date=brigade.date,

        )
        return Response ({"detail": "Report Compiled and submitted to HQ"}, status=status.HTTP_200_OK)
    
    def compile_pdf(self, submissions):
        # pdf compilation logic
        pass


class UnitViewSet(viewsets.ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer

class BrigadeViewSet(viewsets.ModelViewSet):
    queryset = Brigade.objects.all()
    serializer_class = BrigadeSerializer
