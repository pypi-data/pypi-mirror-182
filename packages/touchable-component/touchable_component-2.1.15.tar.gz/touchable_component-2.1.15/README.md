# touchable component

touchable component is a Dash component library.
Component to acquire coordinates and movements for smartphones.

### Installation
***

    ```
    $ pip install touchable_component
    ```

### Properties
***

- children (dash component)
- id (string)
- className (string)
- n_clicks (int)
- direction (string; readonly)

    Flick-swipe direction.
    - up
    - down
    - left
    - right

- flick (float; readonly)

    Timestamp at end of flick operation.

- swipe (float; readonly)

    Timestamp at end of swipe operation.

- long_tap (float; readonly)

    Timestamp of the start of the long press.

- long_tap_end (float; readonly)

    Timestamp of the end of the long press.

- long_swipe (float; readonly)

    Timestamp when swiped after long press.
- start_timestamp (float; readonly)

    Timestamp of the start of the touch.

- end_timestamp (float; readonly)

    Timestamp of the end of the touch.

- touches (list[dict]; readonly)
    List of coordinate information.
    - x
        x-coordinate in component.
    - y
        y-coordinate in component.
    - clientX
        Relative x-coordinates, not including the scroll offset from the viewport of the touch points.
    - clientY
        Relative y-coordinates, not including the scroll offset from the viewport of the touch points.
    - top
        Relative position of the upper left corner of the browser's display area as a base point.
    - left
        Relative position of the upper left corner of the browser's display area as a base point.