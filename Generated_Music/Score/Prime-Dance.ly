\version "2.26.0"

\header {
  title = "Prime dance"
  instrument = "for flute"
  composer = "Jan Tamzejian"
  opus = "Op. 26"
  copyright = "CC-By-ND-NC 2026"
  tagline = "Musicamath"
}

\paper {
  #(set-paper-size "a4")
  % Add space for instrument names
  indent = 18\mm
}

global = {
  \key c \major
  \time 4/4
  \tempo "Tempo giusto" 4=128
}

myScore = \include"prime_music_edited.ly"

flute = \transpose c c'{
%flute = { % ly-to-xml do not supprot transpose statement ! (consider file to be empty)
  \global
  \myScore
}

\score {
  \new Staff \with {
    instrumentName = "Flûte"
    midiInstrument = "flute"
  } \flute
  \layout { }
}

\score {
  \new Staff \with {
    instrumentName = "Flûte"
    midiInstrument = "flute"
  } \flute
  \midi { }
}
