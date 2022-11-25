import string, random

from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .middleware import tmp
from django.utils.text import slugify


class RdFullName:
    FIRST_ARR = [
        'Nguyễn', 'Trần', 'Lê', 'Phạm', 'Huỳnh', 'Hoàng', 'Võ', 'Vũ', 'Phan', 'Trương', 'Bùi', 'Đặng', 'Đỗ',
        'Ngô', 'Hồ', 'Dương', 'Đinh', 'Đoàn', 'Lâm', 'Mai', 'Trịnh', 'Đào', 'Cao', 'Lý', 'Hà', 'Lưu', 'Lương',
        'Thái', 'Châu', 'Tạ', 'Phùng', 'Tô', 'Vương', 'Văn', 'Tăng', 'Quách', 'Lại', 'Hứa', 'Thạch', 'Diệp',
        'Từ', 'Chu', 'La', 'Đàm', 'Tống', 'Giang', 'Chung', 'Triệu', 'Kiều', 'Hồng', 'Trang', 'Đồng', 'Danh',
        'Lư', 'Lữ', 'Thân', 'Kim', 'Mã', 'Bạch', 'Liêu', 'Tiêu', 'Dư', 'Bành', 'Âu', 'Tôn', 'Khưu', 'Sơn',
        'Tất', 'Nghiêm', 'Lục', 'Quan', 'Phương', 'Mạc', 'Lai', 'Vòng', 'Mạch', 'Thiều', 'Trà', 'Đậu', 'Nhan',
        'Lã', 'Trình', 'Ninh', 'Trầm', 'Vi', 'Biện', 'Hàng', 'Ôn', 'Chế', 'Nhâm', 'Tôn Nữ', 'Thi', 'Doãn',
        'Khổng', 'Phù', 'Đường', 'Ông', 'Tôn Thất', 'Ngụy', 'Viên', 'Tào', 'Cù'
    ]
    MIDDLE_ARR = [
        'Bá', 'Mạnh', 'Trọng', 'Thúc', 'Quý',
        'Văn', 'Thanh', 'Gia', 'Minh', 'Hùng',
        'Sơn', 'Kiên', 'Nhân', 'Quốc', 'Đức',
        'Hải', 'Tâm', 'Bá',
    ]
    LAST_ARR = [
        'Huy', 'Khang', 'Bảo', 'Minh', 'Phúc', 'Anh', 'Khoa', 'Phát', 'Đạt', 'Khôi', 'Long', 'Nam', 'Duy', 'Quân',
        'Kiệt', 'Thịnh', 'Tuấn', 'Hưng', 'Hoàng', 'Hiếu', 'Nhân', 'Trí', 'Tài', 'Phong', 'Nguyên', 'An', 'Phú',
        'Thành', 'Đức', 'Dũng', 'Lộc', 'Khánh', 'Vinh', 'Tiến', 'Nghĩa', 'Thiện', 'Hào', 'Hải', 'Đăng', 'Quang', 'Lâm',
        'Nhật', 'Trung', 'Thắng', 'Tú', 'Hùng', 'Tâm', 'Sang', 'Sơn', 'Thái', 'Cường', 'Vũ', 'Toàn', 'Ân', 'Thuận',
        'Bình', 'Trường', 'Danh', 'Kiên', 'Phước', 'Thiên', 'Tân', 'Việt', 'Khải', 'Tín', 'Dương', 'Tùng', 'Quý',
        'Hậu', 'Trọng', 'Triết', 'Luân', 'Phương', 'Quốc', 'Thông', 'Khiêm', 'Hòa', 'Thanh', 'Tường', 'Kha', 'Vỹ',
        'Bách', 'Khanh', 'Mạnh', 'Lợi', 'Đại', 'Hiệp', 'Đông', 'Nhựt', 'Giang', 'Kỳ', 'Phi', 'Tấn', 'Văn', 'Vương',
        'Công', 'Hiển', 'Linh', 'Ngọc', 'Vĩ'
    ]

    def get_full_name(self):
        return f'{random.choice(self.FIRST_ARR)} {random.choice(self.MIDDLE_ARR)} {random.choice(self.LAST_ARR)}'


class ViewTest(APIView):
    def get(self, request, *args, **kwargs):
        if 'id_user' not in request.session:
            rd_full = RdFullName().get_full_name()
            rd_str = slugify(rd_full)
            request.session['id_user'] = rd_str
            tmp[rd_str] = rd_full
        return render(request, 'index.html', {
            'id': request.session.get('id_user', 'NaN'),
            'name': request.session.get('name_user', 'NaN'),
        })


class PageTest(APIView):
    def get(self, request, *args, **kwargs):
        return render(request, 'page.html', {
            'id': request.session.get('id_user', 'NaN'),
            'name': request.session.get('name_user', 'NaN'),
        })
