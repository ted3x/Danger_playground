package ge.ted3x.dangerplayground

import android.hardware.Camera
import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity

class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        Camera.ACTION_NEW_PICTURE
    }
}
