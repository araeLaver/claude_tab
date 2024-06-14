const fileInput = document.getElementById('file-input');
const dropArea = document.querySelector('.drop-area');
const preview = document.getElementById('preview');
const form = document.querySelector('form');

// 파일 선택 이벤트 처리
fileInput.addEventListener('change', updatePreview);

// 드래그 앤 드롭 이벤트 처리
['dragenter', 'dragover', 'dragleave', 'drop'].forEach(evt => {
    dropArea.addEventListener(evt, preventDefaults, false);
});

dropArea.addEventListener('drop', handleDrop, false);

function updatePreview() {
    preview.innerHTML = '';
    [...fileInput.files].forEach(uploadedFile => {
        const img = document.createElement('img');
        img.src = URL.createObjectURL(uploadedFile);
        preview.appendChild(img);

        // 이미지 파일을 Base64로 인코딩
        const reader = new FileReader();
        reader.onload = () => {
            const base64Image = reader.result.split(',')[1];
            // Base64 인코딩된 이미지 데이터를 폼 데이터에 추가
            const formData = new FormData(form);
            formData.append('image', base64Image);
        };
        reader.readAsDataURL(uploadedFile);
    });
}

function preventDefaults(e) {
    e.preventDefault();
    e.stopPropagation();
}

function handleDrop(e) {
    const dt = e.dataTransfer;
    const files = dt.files;
    handleFiles(files);
}

function handleFiles(files) {
    fileInput.files = files;
    updatePreview();
}

// 폼 제출 이벤트 처리
form.addEventListener('submit', (e) => {
    e.preventDefault();
    const formData = new FormData(form);
    // Flask 백엔드로 폼 데이터 전송
    fetch('/', {
        method: 'POST',
        body: formData
    })
    .then(response => response.text())
    .then(data => {
        // 응답 처리
        console.log(data);
    })
    .catch(error => {
        console.error('Error:', error);
    });
});