function playPreview(audioId) {
    // Pause all audio elements
    const audios = document.querySelectorAll('audio');
    audios.forEach(audio => {
        audio.pause();
        audio.currentTime = 0; // Reset playback position
    });

    // Play the selected audio
    const audio = document.getElementById(audioId);
    audio.play();
}