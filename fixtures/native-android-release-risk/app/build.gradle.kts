import java.io.FileInputStream
import java.util.Properties
import org.gradle.api.GradleException

plugins {
    id("com.android.application")
    id("org.jetbrains.kotlin.android")
}

val keystorePropertiesFile = rootProject.file("key.properties")
val keystoreProperties = Properties()
val hasRequiredKeystoreProperties = if (keystorePropertiesFile.exists()) {
    keystoreProperties.load(FileInputStream(keystorePropertiesFile))
    keystoreProperties.containsKey("keyAlias") &&
        keystoreProperties.containsKey("keyPassword") &&
        keystoreProperties.containsKey("storeFile") &&
        keystoreProperties.containsKey("storePassword")
} else {
    false
}
val releaseStoreFile = keystoreProperties.getProperty("storeFile")?.let { rootProject.file(it) }
val hasValidKeystore = hasRequiredKeystoreProperties && releaseStoreFile?.exists() == true

android {
    namespace = "com.example.nativeandroidfixture"
    compileSdk = 35

    defaultConfig {
        applicationId = "com.example.nativeandroidfixture"
        minSdk = 24
        targetSdk = 35
        versionCode = 8
        versionName = "1.1.0"
    }

    signingConfigs {
        if (hasValidKeystore) {
            create("release") {
                keyAlias = keystoreProperties["keyAlias"] as String
                keyPassword = keystoreProperties["keyPassword"] as String
                storeFile = file(keystoreProperties["storeFile"] as String)
                storePassword = keystoreProperties["storePassword"] as String
            }
        }
    }

    buildTypes {
        release {
            if (hasValidKeystore) {
                signingConfig = signingConfigs.getByName("release")
            }
            isMinifyEnabled = true
        }
    }
}

gradle.taskGraph.whenReady {
    val buildsReleaseArtifact = allTasks.any { task ->
        val taskName = task.name
        taskName.contains("Release") &&
            (taskName.startsWith("assemble") ||
                taskName.startsWith("bundle") ||
                taskName.startsWith("package"))
    }

    if (buildsReleaseArtifact && !hasValidKeystore) {
        throw GradleException(
            "Release signing is not configured. Add key.properties with " +
                "keyAlias, keyPassword, storeFile, and storePassword."
        )
    }
}
