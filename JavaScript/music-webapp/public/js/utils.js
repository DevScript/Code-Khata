function playpauseTrack() {
  if (!isPlaying) playTrack();
  else pauseTrack();
}

// play music function
function playTrack() {
  musicObj.play();
  isPlaying = true;
  playPauseBtn.innerHTML = '<i class="fa fa-pause-circle fa-5x"></i>';
}

// pause music function
function pauseTrack() {
  musicObj.pause();
  isPlaying = false;
  playPauseBtn.innerHTML = '<i class="fa fa-play-circle fa-5x"></i>';
}

// change title
function changeMusicTitle(name) {
  if (name != undefined) {
    musicTitle.innerHTML = name;
  }
}

// reset music timer
function resetMusicTimer() {
  currentTime.innerHTML = "00:00";
  endTime.innerHTML = "00:00";
  musicSlider.value = 0;
}

// update music slider
function updateMusicSlider() {
  let musicPos = 0;
  if (musicObj.duration != musicObj.currentTime) {
    let instantTime = Math.ceil(musicObj.currentTime);
    let duration = Math.ceil(musicObj.duration);
    let durationMin = Math.floor(duration / 60);
    let durationSec = Math.floor(duration % 60);

    let currentMin = Math.floor(instantTime / 60);
    let currentSec = Math.floor(instantTime % 60);

    musicPos = (instantTime * 100) / duration;

    musicSlider.value = musicPos;

    // for palying time
    if (currentSec < 10) {
      currentTime.innerHTML = `0${currentMin}:0${currentSec}`;
    } else {
      currentTime.innerHTML = `0${currentMin}:${currentSec}`;
    }

    // for duration
    if (durationSec != NaN) {
      if (durationSec < 10) {
        endTime.innerHTML = `0${durationMin}:0${durationSec}`;
      } else {
        endTime.innerHTML = `0${durationMin}:${durationSec}`;
      }
    }
  } else {
    resetMusicTimer();
    pauseTrack();
  }
}

// for changing music position
function changeMusicPos() {
  let changedSliderPos = musicSlider.value;
  let changedMusicPos = (changedSliderPos * musicObj.duration) / 100;
  musicObj.currentTime = changedMusicPos;
}

// change prev next btn color
function changePrevNextColor() {
  let position = dll.nodePosition();

  if (position === 1) {
    prevBtn.style.color = "black";
    nextBtn.style.color = "white";
  } else if (position === -1) {
    prevBtn.style.color = "white";
    nextBtn.style.color = "black";
  } else {
    prevBtn.style.color = "white";
    nextBtn.style.color = "white";
  }
}
