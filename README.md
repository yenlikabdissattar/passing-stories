# Passing Stories

A history map of Sinchon, Seoul: walk around Yonsei, Ewha and Sinchon station and read what happened where.
Team 5 hi-fi prototype for the Interaction Design course (Yonsei UIC, Fall 2026).

**Open it:** https://yenlikabdissattar.github.io/passing-stories/

- On a phone it fills the screen like an app. In Safari use Share > Add to Home Screen (Chrome: menu > Add to Home screen) to open it full screen.
- On a laptop you see the phone next to a list of every screen.

This is a class demo with sample data. Field notes (beta) are stored only in your own browser. Please don't enter personal information.

## Sinchon Archive Finds (updated daily)

**Open it:** https://yenlikabdissattar.github.io/passing-stories/archive/

Public-archive records about the Sinchon area (photos, maps, documents) that a scheduled collector finds every day. The page reads `archive/finds.json`, which the collector rewrites and pushes after each run with `archive/build_finds.py`.

Every record, image and description comes from the source named on its entry (mainly the Seoul Historical Archive / Seoul Museum of History). Rights stay with those sources and reuse follows each record's licence. English titles and notes are our translations. Passing Stories takes no responsibility for what these sources deliver; check the original record before using anything.

The images in `archive/img/` are copies of the archive's own preview images (KOGL Type 1, except two KOGL Type 2 plans), credited to the Seoul Museum of History on every view.

## What's inside

- Map of Sinchon you can drag and zoom, with 21 history pins (13 stories + 8 added from the archive) and walking routes
- Archive button: all 93 Seoul Historical Archive records about Sinchon, filtered by photos, maps and decade, each opening full size with its source link. Place cards show the archive photos for that spot. Images are saved in `archive/img/`.
- Era button: 1942, 1927 and 1861 maps, and the 1420s (King Sejong's Yeonhuigung)
- Detailed, Simple and Terrain (contour) map styles
- English and Korean (EN / 한 button)
- Field notes beta: take a photo, write a short note

## Credits

- Archive photos and historical maps: Seoul Museum of History, Seoul Historical Archive (서울역사아카이브), KOGL Type 1 (credit the source). Record numbers are shown in the app. The 1861 map (srd-415198) is from the museum collection; its licence still needs checking on its record page.
- Building photos: Korea Heritage Service (국가유산청)
- Base maps: © Mapbox © OpenStreetMap contributors. Walking distances: Mapbox Directions.
- Map library: Leaflet 1.9.4 (BSD-2-Clause), included in the page.
