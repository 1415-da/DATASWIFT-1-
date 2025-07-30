/** @type {import('next').NextConfig} */
const nextConfig = {
  eslint: {
    ignoreDuringBuilds: true,
  },
  typescript: {
    ignoreBuildErrors: true,
  },
  images: {
    unoptimized: true,
  },
  async rewrites() {
    return [
      {
        source: '/api/data/:path*',
        destination: process.env.NEXT_PUBLIC_BACKEND_URL + '/api/data/:path*',
      },
      {
        source: '/api/model/:path*',
        destination: process.env.NEXT_PUBLIC_BACKEND_URL + '/api/model/:path*',
      },
      {
        source: '/api/predict/:path*',
        destination: process.env.NEXT_PUBLIC_BACKEND_URL + '/api/predict/:path*',
      },
      {
        source: '/api/knowledge/:path*',
        destination: process.env.NEXT_PUBLIC_BACKEND_URL + '/api/knowledge/:path*',
      },
      {
        source: '/api/user/:path*',
        destination: process.env.NEXT_PUBLIC_BACKEND_URL + '/api/user/:path*',
      },
    ];
  },
}

export default nextConfig
