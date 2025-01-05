import asyncio
from crawl4ai import AsyncWebCrawler

async def main():
    async with AsyncWebCrawler(verbose = True) as crawler:
        result = await crawler.arun(url='cnnportugal.iol.pt/pais')
        print(result.markdown)

if __name__ == '__main__':
    asyncio.run(main())