# Blend_and_Share

## Description

## Project requirments

## User stories

## Design

### Colour scheme

### Typography

### Wireframe

## Technologies used

## Tools used

## Deployment

## Testing

## Bugs and Fixes

**Issue:** *ModuleNotFoundError: smoothies.forms not found.*

**Solution:** *The forms.py was accidentally saved inside templates folder. Moved forms.py into the app directory.*

---

**Issue:** *The smoothie model was missing the description field.*

**Solution:** *Added the correct line to the model.*

---

**Issue:** *'smoothies.views' had no attribute 'signup'.*

**Solution:** *Added the signup() function in views.py using UserCreationForm.*

---

**Issue:** *No Reverse Match error.*

**Solution:** *Added the proper path for 'smoothie create'.*

---

**Issue:** *URL pattern syntax error: Unmatched brackets in the smoothie update and smoothie delete URL patterns.*

**Solution:** *Closed the angle brackets properly in urls.py*

## Credits

---

**Issue:** *When trying to load the form page a template syntax error appeared.*

**Solution:** *The form was incorrectly written using {% form.as_p %}. I changed it to curly braces for variables.*
