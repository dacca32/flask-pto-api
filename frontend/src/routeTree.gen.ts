/* eslint-disable */

// @ts-nocheck

// noinspection JSUnusedGlobalSymbols

// This file was automatically generated by TanStack Router.
// You should NOT make any changes in this file as it will be overwritten.
// Additionally, you should also exclude this file from your linter and/or formatter to prevent it from being checked or modified.

// Import Routes

import { Route as rootRoute } from './routes/__root'
import { Route as RegisterIndexImport } from './routes/register/index'
import { Route as ProfileIndexImport } from './routes/profile/index'
import { Route as LoginIndexImport } from './routes/login/index'
import { Route as HomeIndexImport } from './routes/home/index'

// Create/Update Routes

const RegisterIndexRoute = RegisterIndexImport.update({
  id: '/register/',
  path: '/register/',
  getParentRoute: () => rootRoute,
} as any)

const ProfileIndexRoute = ProfileIndexImport.update({
  id: '/profile/',
  path: '/profile/',
  getParentRoute: () => rootRoute,
} as any)

const LoginIndexRoute = LoginIndexImport.update({
  id: '/login/',
  path: '/login/',
  getParentRoute: () => rootRoute,
} as any)

const HomeIndexRoute = HomeIndexImport.update({
  id: '/home/',
  path: '/home/',
  getParentRoute: () => rootRoute,
} as any)

// Populate the FileRoutesByPath interface

declare module '@tanstack/react-router' {
  interface FileRoutesByPath {
    '/home/': {
      id: '/home/'
      path: '/home'
      fullPath: '/home'
      preLoaderRoute: typeof HomeIndexImport
      parentRoute: typeof rootRoute
    }
    '/login/': {
      id: '/login/'
      path: '/login'
      fullPath: '/login'
      preLoaderRoute: typeof LoginIndexImport
      parentRoute: typeof rootRoute
    }
    '/profile/': {
      id: '/profile/'
      path: '/profile'
      fullPath: '/profile'
      preLoaderRoute: typeof ProfileIndexImport
      parentRoute: typeof rootRoute
    }
    '/register/': {
      id: '/register/'
      path: '/register'
      fullPath: '/register'
      preLoaderRoute: typeof RegisterIndexImport
      parentRoute: typeof rootRoute
    }
  }
}

// Create and export the route tree

export interface FileRoutesByFullPath {
  '/home': typeof HomeIndexRoute
  '/login': typeof LoginIndexRoute
  '/profile': typeof ProfileIndexRoute
  '/register': typeof RegisterIndexRoute
}

export interface FileRoutesByTo {
  '/home': typeof HomeIndexRoute
  '/login': typeof LoginIndexRoute
  '/profile': typeof ProfileIndexRoute
  '/register': typeof RegisterIndexRoute
}

export interface FileRoutesById {
  __root__: typeof rootRoute
  '/home/': typeof HomeIndexRoute
  '/login/': typeof LoginIndexRoute
  '/profile/': typeof ProfileIndexRoute
  '/register/': typeof RegisterIndexRoute
}

export interface FileRouteTypes {
  fileRoutesByFullPath: FileRoutesByFullPath
  fullPaths: '/home' | '/login' | '/profile' | '/register'
  fileRoutesByTo: FileRoutesByTo
  to: '/home' | '/login' | '/profile' | '/register'
  id: '__root__' | '/home/' | '/login/' | '/profile/' | '/register/'
  fileRoutesById: FileRoutesById
}

export interface RootRouteChildren {
  HomeIndexRoute: typeof HomeIndexRoute
  LoginIndexRoute: typeof LoginIndexRoute
  ProfileIndexRoute: typeof ProfileIndexRoute
  RegisterIndexRoute: typeof RegisterIndexRoute
}

const rootRouteChildren: RootRouteChildren = {
  HomeIndexRoute: HomeIndexRoute,
  LoginIndexRoute: LoginIndexRoute,
  ProfileIndexRoute: ProfileIndexRoute,
  RegisterIndexRoute: RegisterIndexRoute,
}

export const routeTree = rootRoute
  ._addFileChildren(rootRouteChildren)
  ._addFileTypes<FileRouteTypes>()

/* ROUTE_MANIFEST_START
{
  "routes": {
    "__root__": {
      "filePath": "__root.tsx",
      "children": [
        "/home/",
        "/login/",
        "/profile/",
        "/register/"
      ]
    },
    "/home/": {
      "filePath": "home/index.tsx"
    },
    "/login/": {
      "filePath": "login/index.tsx"
    },
    "/profile/": {
      "filePath": "profile/index.tsx"
    },
    "/register/": {
      "filePath": "register/index.tsx"
    }
  }
}
ROUTE_MANIFEST_END */
