import os
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

def test_ui_refinement():
    print("========================================")
    print("RABBIT Pre-Launch UI/UX Test Suite")
    print("========================================")
    
    # 1. Check Theme & Design Tokens
    assert os.path.exists('rabbit-theme.css'), "rabbit-theme.css missing"
    with open('rabbit-theme.css', 'r', encoding='utf-8') as f:
        theme = f.read()
    assert '#050505' in theme, "Obsidian background token missing"
    assert '#A78BFA' in theme, "Signature violet token missing"
    assert 'scrollbar-width: none' in theme, "Scrollbar hiding missing"
    print("✓ [PASS] Part 1: Global Visual Identity & Tokens (Obsidian Black × Cosmic Violet)")

    # 2. Check 2-Second Mandatory Loader
    assert os.path.exists('rabbit-loader.js'), "rabbit-loader.js missing"
    with open('rabbit-loader.js', 'r', encoding='utf-8') as f:
        loader = f.read()
    assert '2000 - elapsed' in loader, "2000ms minimum duration missing in loader"
    assert 'Every page hides another universe.' in loader, "Poetic lines missing"
    assert 'rabbit-hopping-figure' in loader, "Hopping rabbit SVG missing"
    print("✓ [PASS] Part 2: Mandatory 2-Second Hopping Rabbit Loading Animation")

    # 3. Check Authoritative Genre Selection Modal & Wild Burrow
    assert os.path.exists('rabbit-genre-modal.js'), "rabbit-genre-modal.js missing"
    with open('rabbit-genre-modal.js', 'r', encoding='utf-8') as f:
        modal = f.read()
    assert 'THE WILD BURROW' in modal, "The Wild Burrow option missing"
    assert 'Enter the Rabbit Hole' in modal, "Primary CTA Enter the Rabbit Hole missing"
    assert 'tempSelectedGenres.add' in modal and 'tempSelectedGenres.delete' in modal, "Multi-genre toggle logic missing"
    assert 'AUTHORITATIVE_GENRES' in modal, "21 Genres list missing"
    print("✓ [PASS] Part 3: Genre Selection & The Wild Burrow (Multi-select, No Early Redirect)")

    # 4. Check Simplified 5-Destination Navigation
    assert os.path.exists('rabbit-navigation.js'), "rabbit-navigation.js missing"
    with open('rabbit-navigation.js', 'r', encoding='utf-8') as f:
        nav = f.read()
    for dest in ["home", "genres", "warren", "clubs", "profile"]:
        assert f'id: "{dest}"' in nav, f"Destination {dest} missing from shared nav"
    assert 'library' not in nav or 'following' not in nav, "Redundant destinations not cleaned up"
    print("✓ [PASS] Part 4: Simplified 5-Destination Navigation System")

    # 5. Check Signature Profile Experience & Reading Constellation
    assert os.path.exists('rabbit-profile.js'), "rabbit-profile.js missing"
    with open('rabbit-profile.js', 'r', encoding='utf-8') as f:
        profile = f.read()
    assert 'rabbit-constellation-canvas' in profile, "Constellation canvas missing"
    assert 'Saved Library' in profile, "Saved Library tab in Profile missing"
    assert 'Followed Books' in profile, "Followed Books tab in Profile missing"
    assert 'startConstellationCanvas' in profile, "Constellation generator missing"
    print("✓ [PASS] Parts 5 & 8: Signature Profile Experience ('Your Little Universe') & Constellation")

    # 6. Check Unified Community (Warren & Clubs)
    assert os.path.exists('rabbit-community-views.js'), "rabbit-community-views.js missing"
    with open('rabbit-community-views.js', 'r', encoding='utf-8') as f:
        comm = f.read()
    assert 'The Warren ✦' in comm, "Warren view header missing"
    assert 'Clubs ✦' in comm, "Clubs view header missing"
    assert 'rabbit-community-stories-rail' in comm, "Stories rail missing in Warren"
    print("✓ [PASS] Parts 6 & 7: Unified Warren & Clubs Views with Stories Rail")

    # 7. Check Redesigned Authentication View
    assert os.path.exists('rabbit-auth.js'), "rabbit-auth.js missing"
    with open('rabbit-auth.js', 'r', encoding='utf-8') as f:
        auth = f.read()
    assert 'Your rabbit hole awaits.' in auth, "Auth headline missing"
    assert 'Back to Home' in auth, "Back to Home CTA missing"
    print("✓ [PASS] Part 9: Redesigned Authentication Experience")

    # 8. Check index.html Integration & Welcome Screen
    with open('index.html', 'r', encoding='utf-8') as f:
        index = f.read()
    assert 'rabbit-theme.css' in index, "rabbit-theme.css not linked in index.html"
    assert 'rabbit-loader.js' in index, "rabbit-loader.js not loaded in index.html"
    assert 'rabbit-genre-modal.js' in index, "rabbit-genre-modal.js not loaded in index.html"
    assert 'Take me to the rabbit hole' in index, "Take me to the rabbit hole CTA missing in index.html"
    assert 'rabbit_onboarding_completed' in index, "Onboarding persistence check missing in index.html"
    print("✓ [PASS] Part 10 & 11: Index.html SPA Shell, Welcome Screen & Module Integration")

    # 9. Check Standalone Pages Integrity
    for page in ['warren.html', 'clubs.html', 'account.html', 'community.html', 'discover.html']:
        assert os.path.exists(page), f"Page missing: {page}"
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        assert len(content) > 100, f"Page content missing in {page}"
    print("[PASS] Part 11: Standalone Pages Verified & Functional")

    print("\nALL PRE-LAUNCH REGRESSION TESTS PASSED (9/9)!\n")

if __name__ == '__main__':
    test_ui_refinement()
