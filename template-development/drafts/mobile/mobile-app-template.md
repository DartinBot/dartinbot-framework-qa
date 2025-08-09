# DartinBot Mobile App Development Template

<dartinbot-template 
    name="Mobile App Development Template"
    category="mobile"
    version="3.0.0"
    framework-version="3.0.0"
    scope="cross-platform-mobile-app"
    difficulty="intermediate"
    confidence-score="0.88"
    auto-improve="true">

## Project Overview
<dartinbot-detect>
Target: Cross-platform mobile application development
Tech Stack: React Native, TypeScript, Expo
Purpose: Build native mobile apps for iOS and Android with shared codebase
</dartinbot-detect>

## Tech Stack Configuration
<dartinbot-brain 
    specialty="mobile-development"
    model="gpt-4"
    focus="react-native,expo,typescript,mobile-ui"
    expertise-level="intermediate">

### Core Technologies
- **Framework**: React Native with Expo
- **Language**: TypeScript for type safety
- **Navigation**: React Navigation v6
- **State Management**: Zustand with AsyncStorage
- **UI Components**: NativeBase / Tamagui
- **Testing**: Jest, React Native Testing Library, Detox

### Platform Support
- **iOS**: Native iOS development support
- **Android**: Native Android development support
- **Web**: Progressive Web App (PWA) support
- **Development**: Expo Go for rapid prototyping
- **Build**: EAS Build for production deployments

### Backend Integration
- **API Client**: Axios with TypeScript definitions
- **Authentication**: Expo AuthSession, Firebase Auth
- **Storage**: AsyncStorage, SecureStore
- **Push Notifications**: Expo Notifications
- **Analytics**: Expo Analytics, Firebase Analytics

## Project Structure

### Core Application Structure
```
mobile-app/
├── src/
│   ├── components/
│   │   ├── common/
│   │   │   ├── Button.tsx
│   │   │   ├── Input.tsx
│   │   │   └── LoadingSpinner.tsx
│   │   ├── forms/
│   │   │   ├── LoginForm.tsx
│   │   │   └── ProfileForm.tsx
│   │   └── navigation/
│   │       ├── TabNavigator.tsx
│   │       └── StackNavigator.tsx
│   ├── screens/
│   │   ├── auth/
│   │   │   ├── LoginScreen.tsx
│   │   │   └── RegisterScreen.tsx
│   │   ├── main/
│   │   │   ├── HomeScreen.tsx
│   │   │   ├── ProfileScreen.tsx
│   │   │   └── SettingsScreen.tsx
│   │   └── onboarding/
│   │       └── WelcomeScreen.tsx
│   ├── services/
│   │   ├── api/
│   │   │   ├── authApi.ts
│   │   │   ├── userApi.ts
│   │   │   └── apiClient.ts
│   │   ├── storage/
│   │   │   ├── secureStorage.ts
│   │   │   └── asyncStorage.ts
│   │   └── notifications/
│   │       └── pushNotifications.ts
│   ├── store/
│   │   ├── authStore.ts
│   │   ├── userStore.ts
│   │   └── settingsStore.ts
│   ├── utils/
│   │   ├── constants.ts
│   │   ├── helpers.ts
│   │   └── validators.ts
│   ├── hooks/
│   │   ├── useAuth.ts
│   │   ├── useApi.ts
│   │   └── useNotifications.ts
│   └── types/
│       ├── auth.ts
│       ├── user.ts
│       └── api.ts
├── assets/
│   ├── images/
│   ├── icons/
│   └── fonts/
└── __tests__/
    ├── components/
    ├── screens/
    └── services/
```

## Configuration Files

### Expo Configuration
<dartinbot-config type="app.json">
```json
{
  "expo": {
    "name": "MyMobileApp",
    "slug": "my-mobile-app",
    "version": "1.0.0",
    "orientation": "portrait",
    "icon": "./assets/icon.png",
    "userInterfaceStyle": "automatic",
    "splash": {
      "image": "./assets/splash.png",
      "resizeMode": "contain",
      "backgroundColor": "#ffffff"
    },
    "assetBundlePatterns": [
      "**/*"
    ],
    "ios": {
      "supportsTablet": true,
      "bundleIdentifier": "com.mycompany.mymobileapp",
      "buildNumber": "1.0.0"
    },
    "android": {
      "adaptiveIcon": {
        "foregroundImage": "./assets/adaptive-icon.png",
        "backgroundColor": "#FFFFFF"
      },
      "package": "com.mycompany.mymobileapp",
      "versionCode": 1
    },
    "web": {
      "favicon": "./assets/favicon.png"
    },
    "plugins": [
      "expo-notifications",
      "expo-secure-store",
      "expo-auth-session"
    ]
  }
}
```
</dartinbot-config>

### TypeScript Configuration
<dartinbot-config type="tsconfig.json">
```json
{
  "extends": "expo/tsconfig.base",
  "compilerOptions": {
    "strict": true,
    "baseUrl": "./src",
    "paths": {
      "@components/*": ["components/*"],
      "@screens/*": ["screens/*"],
      "@services/*": ["services/*"],
      "@store/*": ["store/*"],
      "@utils/*": ["utils/*"],
      "@hooks/*": ["hooks/*"],
      "@types/*": ["types/*"]
    }
  },
  "include": [
    "src/**/*"
  ]
}
```
</dartinbot-config>

### Package.json Dependencies
<dartinbot-config type="package.json">
```json
{
  "name": "mobile-app",
  "scripts": {
    "start": "expo start",
    "android": "expo start --android",
    "ios": "expo start --ios",
    "web": "expo start --web",
    "test": "jest",
    "test:watch": "jest --watch",
    "test:e2e": "detox test",
    "build:android": "eas build --platform android",
    "build:ios": "eas build --platform ios",
    "submit": "eas submit"
  },
  "dependencies": {
    "expo": "~49.0.0",
    "expo-status-bar": "~1.6.0",
    "react": "18.2.0",
    "react-native": "0.72.6",
    "@react-navigation/native": "^6.1.0",
    "@react-navigation/stack": "^6.3.0",
    "@react-navigation/bottom-tabs": "^6.5.0",
    "react-native-screens": "~3.22.0",
    "react-native-safe-area-context": "4.6.3",
    "zustand": "^4.4.0",
    "axios": "^1.5.0",
    "expo-notifications": "~0.20.0",
    "expo-secure-store": "~12.3.0",
    "expo-auth-session": "~5.0.0",
    "native-base": "^3.4.0"
  },
  "devDependencies": {
    "@babel/core": "^7.20.0",
    "@types/react": "~18.2.14",
    "@types/react-native": "~0.72.2",
    "typescript": "^5.1.3",
    "jest": "^29.2.1",
    "@testing-library/react-native": "^12.0.0",
    "detox": "^20.0.0"
  }
}
```
</dartinbot-config>

## Core Components

### Reusable Button Component
<dartinbot-component type="button">
```typescript
import React from 'react';
import { TouchableOpacity, Text, StyleSheet, ActivityIndicator } from 'react-native';

interface ButtonProps {
  title: string;
  onPress: () => void;
  variant?: 'primary' | 'secondary' | 'outline';
  disabled?: boolean;
  loading?: boolean;
  fullWidth?: boolean;
}

export const Button: React.FC<ButtonProps> = ({
  title,
  onPress,
  variant = 'primary',
  disabled = false,
  loading = false,
  fullWidth = false,
}) => {
  const buttonStyle = [
    styles.button,
    styles[variant],
    fullWidth && styles.fullWidth,
    disabled && styles.disabled,
  ];

  const textStyle = [
    styles.text,
    styles[`${variant}Text`],
    disabled && styles.disabledText,
  ];

  return (
    <TouchableOpacity
      style={buttonStyle}
      onPress={onPress}
      disabled={disabled || loading}
      activeOpacity={0.8}
    >
      {loading ? (
        <ActivityIndicator color={variant === 'primary' ? '#fff' : '#007AFF'} />
      ) : (
        <Text style={textStyle}>{title}</Text>
      )}
    </TouchableOpacity>
  );
};

const styles = StyleSheet.create({
  button: {
    paddingVertical: 12,
    paddingHorizontal: 24,
    borderRadius: 8,
    alignItems: 'center',
    justifyContent: 'center',
    minHeight: 44,
  },
  primary: {
    backgroundColor: '#007AFF',
  },
  secondary: {
    backgroundColor: '#F2F2F7',
  },
  outline: {
    backgroundColor: 'transparent',
    borderWidth: 1,
    borderColor: '#007AFF',
  },
  fullWidth: {
    width: '100%',
  },
  disabled: {
    opacity: 0.6,
  },
  text: {
    fontSize: 16,
    fontWeight: '600',
  },
  primaryText: {
    color: '#fff',
  },
  secondaryText: {
    color: '#007AFF',
  },
  outlineText: {
    color: '#007AFF',
  },
  disabledText: {
    color: '#8E8E93',
  },
});
```
</dartinbot-component>

### Input Component with Validation
<dartinbot-component type="input">
```typescript
import React, { useState } from 'react';
import { View, TextInput, Text, StyleSheet } from 'react-native';

interface InputProps {
  label?: string;
  placeholder?: string;
  value: string;
  onChangeText: (text: string) => void;
  secureTextEntry?: boolean;
  keyboardType?: 'default' | 'email-address' | 'numeric' | 'phone-pad';
  autoCapitalize?: 'none' | 'sentences' | 'words' | 'characters';
  error?: string;
  required?: boolean;
}

export const Input: React.FC<InputProps> = ({
  label,
  placeholder,
  value,
  onChangeText,
  secureTextEntry = false,
  keyboardType = 'default',
  autoCapitalize = 'none',
  error,
  required = false,
}) => {
  const [isFocused, setIsFocused] = useState(false);

  return (
    <View style={styles.container}>
      {label && (
        <Text style={styles.label}>
          {label}
          {required && <Text style={styles.required}> *</Text>}
        </Text>
      )}
      <TextInput
        style={[
          styles.input,
          isFocused && styles.inputFocused,
          error && styles.inputError,
        ]}
        placeholder={placeholder}
        value={value}
        onChangeText={onChangeText}
        secureTextEntry={secureTextEntry}
        keyboardType={keyboardType}
        autoCapitalize={autoCapitalize}
        onFocus={() => setIsFocused(true)}
        onBlur={() => setIsFocused(false)}
        placeholderTextColor="#8E8E93"
      />
      {error && <Text style={styles.errorText}>{error}</Text>}
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    marginBottom: 16,
  },
  label: {
    fontSize: 16,
    fontWeight: '500',
    marginBottom: 8,
    color: '#1C1C1E',
  },
  required: {
    color: '#FF3B30',
  },
  input: {
    borderWidth: 1,
    borderColor: '#D1D1D6',
    borderRadius: 8,
    paddingVertical: 12,
    paddingHorizontal: 16,
    fontSize: 16,
    backgroundColor: '#fff',
  },
  inputFocused: {
    borderColor: '#007AFF',
  },
  inputError: {
    borderColor: '#FF3B30',
  },
  errorText: {
    color: '#FF3B30',
    fontSize: 14,
    marginTop: 4,
  },
});
```
</dartinbot-component>

## Navigation Setup

### Stack Navigator
<dartinbot-navigation type="stack-navigator">
```typescript
import React from 'react';
import { createStackNavigator } from '@react-navigation/stack';
import { LoginScreen } from '@screens/auth/LoginScreen';
import { RegisterScreen } from '@screens/auth/RegisterScreen';
import { HomeScreen } from '@screens/main/HomeScreen';
import { ProfileScreen } from '@screens/main/ProfileScreen';

export type RootStackParamList = {
  Login: undefined;
  Register: undefined;
  Home: undefined;
  Profile: { userId: string };
};

const Stack = createStackNavigator<RootStackParamList>();

export const AppNavigator: React.FC = () => {
  return (
    <Stack.Navigator
      initialRouteName="Login"
      screenOptions={{
        headerStyle: {
          backgroundColor: '#007AFF',
        },
        headerTintColor: '#fff',
        headerTitleStyle: {
          fontWeight: 'bold',
        },
      }}
    >
      <Stack.Screen
        name="Login"
        component={LoginScreen}
        options={{ headerShown: false }}
      />
      <Stack.Screen
        name="Register"
        component={RegisterScreen}
        options={{ title: 'Sign Up' }}
      />
      <Stack.Screen
        name="Home"
        component={HomeScreen}
        options={{ title: 'Home' }}
      />
      <Stack.Screen
        name="Profile"
        component={ProfileScreen}
        options={{ title: 'Profile' }}
      />
    </Stack.Navigator>
  );
};
```
</dartinbot-navigation>

### Tab Navigator
<dartinbot-navigation type="tab-navigator">
```typescript
import React from 'react';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { Ionicons } from '@expo/vector-icons';
import { HomeScreen } from '@screens/main/HomeScreen';
import { ProfileScreen } from '@screens/main/ProfileScreen';
import { SettingsScreen } from '@screens/main/SettingsScreen';

const Tab = createBottomTabNavigator();

export const TabNavigator: React.FC = () => {
  return (
    <Tab.Navigator
      screenOptions={({ route }) => ({
        tabBarIcon: ({ focused, color, size }) => {
          let iconName: keyof typeof Ionicons.glyphMap;

          if (route.name === 'Home') {
            iconName = focused ? 'home' : 'home-outline';
          } else if (route.name === 'Profile') {
            iconName = focused ? 'person' : 'person-outline';
          } else if (route.name === 'Settings') {
            iconName = focused ? 'settings' : 'settings-outline';
          } else {
            iconName = 'help-outline';
          }

          return <Ionicons name={iconName} size={size} color={color} />;
        },
        tabBarActiveTintColor: '#007AFF',
        tabBarInactiveTintColor: 'gray',
      })}
    >
      <Tab.Screen name="Home" component={HomeScreen} />
      <Tab.Screen name="Profile" component={ProfileScreen} />
      <Tab.Screen name="Settings" component={SettingsScreen} />
    </Tab.Navigator>
  );
};
```
</dartinbot-navigation>

## State Management

### Auth Store with Zustand
<dartinbot-store type="auth-store">
```typescript
import { create } from 'zustand';
import { persist, createJSONStorage } from 'zustand/middleware';
import AsyncStorage from '@react-native-async-storage/async-storage';
import * as SecureStore from 'expo-secure-store';

interface User {
  id: string;
  email: string;
  name: string;
  avatar?: string;
}

interface AuthState {
  user: User | null;
  token: string | null;
  isLoading: boolean;
  isAuthenticated: boolean;
  login: (email: string, password: string) => Promise<void>;
  logout: () => Promise<void>;
  register: (email: string, password: string, name: string) => Promise<void>;
  updateUser: (userData: Partial<User>) => void;
}

export const useAuthStore = create<AuthState>()(
  persist(
    (set, get) => ({
      user: null,
      token: null,
      isLoading: false,
      isAuthenticated: false,

      login: async (email: string, password: string) => {
        set({ isLoading: true });
        
        try {
          // API call to login
          const response = await fetch('/api/auth/login', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password }),
          });

          const data = await response.json();

          if (response.ok) {
            // Store token securely
            await SecureStore.setItemAsync('auth_token', data.token);
            
            set({
              user: data.user,
              token: data.token,
              isAuthenticated: true,
              isLoading: false,
            });
          } else {
            throw new Error(data.message || 'Login failed');
          }
        } catch (error) {
          set({ isLoading: false });
          throw error;
        }
      },

      logout: async () => {
        await SecureStore.deleteItemAsync('auth_token');
        set({
          user: null,
          token: null,
          isAuthenticated: false,
        });
      },

      register: async (email: string, password: string, name: string) => {
        set({ isLoading: true });
        
        try {
          const response = await fetch('/api/auth/register', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ email, password, name }),
          });

          const data = await response.json();

          if (response.ok) {
            await SecureStore.setItemAsync('auth_token', data.token);
            
            set({
              user: data.user,
              token: data.token,
              isAuthenticated: true,
              isLoading: false,
            });
          } else {
            throw new Error(data.message || 'Registration failed');
          }
        } catch (error) {
          set({ isLoading: false });
          throw error;
        }
      },

      updateUser: (userData: Partial<User>) => {
        const { user } = get();
        if (user) {
          set({ user: { ...user, ...userData } });
        }
      },
    }),
    {
      name: 'auth-storage',
      storage: createJSONStorage(() => AsyncStorage),
      partialize: (state) => ({ user: state.user, isAuthenticated: state.isAuthenticated }),
    }
  )
);
```
</dartinbot-store>

## Custom Hooks

### API Hook
<dartinbot-hook type="api-hook">
```typescript
import { useState, useEffect } from 'react';
import { useAuthStore } from '@store/authStore';

interface UseApiOptions {
  immediate?: boolean;
  onSuccess?: (data: any) => void;
  onError?: (error: Error) => void;
}

export const useApi = <T>(
  apiFunction: () => Promise<T>,
  options: UseApiOptions = {}
) => {
  const [data, setData] = useState<T | null>(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<Error | null>(null);
  const { token } = useAuthStore();

  const execute = async () => {
    setLoading(true);
    setError(null);

    try {
      const result = await apiFunction();
      setData(result);
      options.onSuccess?.(result);
    } catch (err) {
      const error = err instanceof Error ? err : new Error('Unknown error');
      setError(error);
      options.onError?.(error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    if (options.immediate && token) {
      execute();
    }
  }, [token]);

  return {
    data,
    loading,
    error,
    execute,
    refetch: execute,
  };
};
```
</dartinbot-hook>

### Notifications Hook
<dartinbot-hook type="notifications-hook">
```typescript
import { useEffect, useRef } from 'react';
import * as Notifications from 'expo-notifications';
import { Platform } from 'react-native';

Notifications.setNotificationHandler({
  handleNotification: async () => ({
    shouldShowAlert: true,
    shouldPlaySound: false,
    shouldSetBadge: false,
  }),
});

export const useNotifications = () => {
  const notificationListener = useRef<any>();
  const responseListener = useRef<any>();

  useEffect(() => {
    registerForPushNotificationsAsync();

    notificationListener.current = Notifications.addNotificationReceivedListener(notification => {
      console.log('Notification received:', notification);
    });

    responseListener.current = Notifications.addNotificationResponseReceivedListener(response => {
      console.log('Notification response:', response);
    });

    return () => {
      Notifications.removeNotificationSubscription(notificationListener.current);
      Notifications.removeNotificationSubscription(responseListener.current);
    };
  }, []);

  const registerForPushNotificationsAsync = async () => {
    if (Platform.OS === 'android') {
      await Notifications.setNotificationChannelAsync('default', {
        name: 'default',
        importance: Notifications.AndroidImportance.MAX,
        vibrationPattern: [0, 250, 250, 250],
        lightColor: '#FF231F7C',
      });
    }

    const { status: existingStatus } = await Notifications.getPermissionsAsync();
    let finalStatus = existingStatus;
    
    if (existingStatus !== 'granted') {
      const { status } = await Notifications.requestPermissionsAsync();
      finalStatus = status;
    }

    if (finalStatus !== 'granted') {
      console.log('Failed to get push token for push notification!');
      return;
    }

    const token = (await Notifications.getExpoPushTokenAsync()).data;
    console.log('Push token:', token);
    return token;
  };

  const sendLocalNotification = async (title: string, body: string) => {
    await Notifications.scheduleNotificationAsync({
      content: {
        title,
        body,
      },
      trigger: null,
    });
  };

  return {
    sendLocalNotification,
  };
};
```
</dartinbot-hook>

## Testing

### Component Testing
<dartinbot-test type="component-test">
```typescript
import React from 'react';
import { render, fireEvent } from '@testing-library/react-native';
import { Button } from '@components/common/Button';

describe('Button Component', () => {
  it('renders correctly with title', () => {
    const { getByText } = render(
      <Button title="Test Button" onPress={() => {}} />
    );
    
    expect(getByText('Test Button')).toBeTruthy();
  });

  it('calls onPress when pressed', () => {
    const mockOnPress = jest.fn();
    const { getByText } = render(
      <Button title="Test Button" onPress={mockOnPress} />
    );
    
    fireEvent.press(getByText('Test Button'));
    expect(mockOnPress).toHaveBeenCalledTimes(1);
  });

  it('shows loading state', () => {
    const { getByTestId } = render(
      <Button title="Test Button" onPress={() => {}} loading={true} />
    );
    
    // ActivityIndicator should be rendered instead of text
    expect(getByTestId('activity-indicator')).toBeTruthy();
  });

  it('is disabled when disabled prop is true', () => {
    const mockOnPress = jest.fn();
    const { getByText } = render(
      <Button title="Test Button" onPress={mockOnPress} disabled={true} />
    );
    
    fireEvent.press(getByText('Test Button'));
    expect(mockOnPress).not.toHaveBeenCalled();
  });
});
```
</dartinbot-test>

### E2E Testing with Detox
<dartinbot-test type="e2e-test">
```typescript
import { device, expect, element, by } from 'detox';

describe('Login Flow', () => {
  beforeAll(async () => {
    await device.launchApp();
  });

  beforeEach(async () => {
    await device.reloadReactNative();
  });

  it('should show login screen', async () => {
    await expect(element(by.id('login-screen'))).toBeVisible();
  });

  it('should login with valid credentials', async () => {
    await element(by.id('email-input')).typeText('test@example.com');
    await element(by.id('password-input')).typeText('password123');
    await element(by.id('login-button')).tap();
    
    await expect(element(by.id('home-screen'))).toBeVisible();
  });

  it('should show error with invalid credentials', async () => {
    await element(by.id('email-input')).typeText('invalid@example.com');
    await element(by.id('password-input')).typeText('wrongpassword');
    await element(by.id('login-button')).tap();
    
    await expect(element(by.id('error-message'))).toBeVisible();
  });
});
```
</dartinbot-test>

## Performance Optimization

### Image Optimization
<dartinbot-optimization type="image-optimization">
```typescript
import React from 'react';
import { Image } from 'expo-image';

interface OptimizedImageProps {
  source: string;
  width: number;
  height: number;
  placeholder?: string;
}

export const OptimizedImage: React.FC<OptimizedImageProps> = ({
  source,
  width,
  height,
  placeholder,
}) => {
  return (
    <Image
      source={{ uri: source }}
      style={{ width, height }}
      placeholder={placeholder}
      contentFit="cover"
      transition={200}
      cachePolicy="memory-disk"
    />
  );
};
```
</dartinbot-optimization>

### List Performance
<dartinbot-optimization type="list-optimization">
```typescript
import React, { useMemo } from 'react';
import { FlatList, ListRenderItem } from 'react-native';

interface OptimizedListProps<T> {
  data: T[];
  renderItem: ListRenderItem<T>;
  keyExtractor: (item: T, index: number) => string;
}

export const OptimizedList = <T,>({
  data,
  renderItem,
  keyExtractor,
}: OptimizedListProps<T>) => {
  const memoizedData = useMemo(() => data, [data]);

  return (
    <FlatList
      data={memoizedData}
      renderItem={renderItem}
      keyExtractor={keyExtractor}
      removeClippedSubviews={true}
      maxToRenderPerBatch={10}
      updateCellsBatchingPeriod={50}
      initialNumToRender={10}
      windowSize={5}
      getItemLayout={(data, index) => ({
        length: 70, // Assuming fixed height items
        offset: 70 * index,
        index,
      })}
    />
  );
};
```
</dartinbot-optimization>

## Error Handling

### Global Error Boundary
<dartinbot-error-handling type="error-boundary">
```typescript
import React, { Component, ReactNode } from 'react';
import { View, Text, TouchableOpacity } from 'react-native';

interface Props {
  children: ReactNode;
}

interface State {
  hasError: boolean;
  error?: Error;
}

export class ErrorBoundary extends Component<Props, State> {
  constructor(props: Props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error: Error): State {
    return { hasError: true, error };
  }

  componentDidCatch(error: Error, errorInfo: any) {
    console.error('Error caught by boundary:', error, errorInfo);
    // Log to crash reporting service
  }

  render() {
    if (this.state.hasError) {
      return (
        <View style={{ flex: 1, justifyContent: 'center', alignItems: 'center', padding: 20 }}>
          <Text style={{ fontSize: 18, fontWeight: 'bold', marginBottom: 10 }}>
            Something went wrong
          </Text>
          <Text style={{ textAlign: 'center', marginBottom: 20 }}>
            We're sorry, but something unexpected happened.
          </Text>
          <TouchableOpacity
            onPress={() => this.setState({ hasError: false })}
            style={{
              backgroundColor: '#007AFF',
              paddingHorizontal: 20,
              paddingVertical: 10,
              borderRadius: 8,
            }}
          >
            <Text style={{ color: 'white' }}>Try Again</Text>
          </TouchableOpacity>
        </View>
      );
    }

    return this.props.children;
  }
}
```
</dartinbot-error-handling>

## Build and Deployment

### EAS Build Configuration
<dartinbot-deployment type="eas.json">
```json
{
  "cli": {
    "version": ">= 3.0.0"
  },
  "build": {
    "development": {
      "developmentClient": true,
      "distribution": "internal"
    },
    "preview": {
      "distribution": "internal",
      "android": {
        "buildType": "apk"
      }
    },
    "production": {
      "android": {
        "buildType": "aab"
      }
    }
  },
  "submit": {
    "production": {
      "android": {
        "serviceAccountKeyPath": "../path/to/api-key.json",
        "track": "internal"
      },
      "ios": {
        "appleId": "your-apple-id@example.com",
        "ascAppId": "1234567890",
        "appleTeamId": "ABCD123456"
      }
    }
  }
}
```
</dartinbot-deployment>

## CI/CD Pipeline

### GitHub Actions for Mobile
<dartinbot-cicd type="github-actions">
```yaml
name: Mobile App CI/CD

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: '18'
          
      - name: Setup Expo
        uses: expo/expo-github-action@v8
        with:
          expo-version: latest
          token: ${{ secrets.EXPO_TOKEN }}
          
      - name: Install dependencies
        run: npm install
        
      - name: Run tests
        run: npm test
        
      - name: Run linting
        run: npx expo lint

  build-android:
    needs: test
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Expo
        uses: expo/expo-github-action@v8
        with:
          expo-version: latest
          token: ${{ secrets.EXPO_TOKEN }}
          
      - name: Build Android
        run: eas build --platform android --non-interactive
        
  build-ios:
    needs: test
    runs-on: macos-latest
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v3
      
      - name: Setup Expo
        uses: expo/expo-github-action@v8
        with:
          expo-version: latest
          token: ${{ secrets.EXPO_TOKEN }}
          
      - name: Build iOS
        run: eas build --platform ios --non-interactive
```
</dartinbot-cicd>

## Next Steps
<dartinbot-auto-improve>
1. **Advanced Navigation**: Deep linking and universal links
2. **Offline Support**: Redux Persist and offline-first architecture
3. **Performance**: Code splitting and lazy loading
4. **Analytics**: User behavior tracking and analytics
5. **Push Notifications**: Advanced notification strategies
6. **Accessibility**: Comprehensive accessibility features
7. **Internationalization**: Multi-language support
8. **Advanced Testing**: Visual regression testing
</dartinbot-auto-improve>

## Troubleshooting Guide
<dartinbot-troubleshooting>
**Common Issues:**
1. **Metro bundler issues**: Clear cache with `npx expo start --clear`
2. **Android build failures**: Check Gradle and SDK versions
3. **iOS build issues**: Verify certificates and provisioning profiles
4. **Navigation problems**: Check navigation dependencies versions
5. **Performance issues**: Use Flipper for debugging and profiling

**Debug Commands:**
- `npx expo doctor` - Check for common issues
- `npx expo install --fix` - Fix dependency versions
- `npx react-native info` - Environment information
- `adb logcat` - Android debugging
- Console logs in Xcode for iOS debugging
</dartinbot-troubleshooting>

</dartinbot-template>
