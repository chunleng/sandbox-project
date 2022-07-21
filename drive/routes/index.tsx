/** @jsx h */
import { h } from "preact";
import { tw } from "@twind";

export default function Home() {
  return (
    <div class={tw`w-full text-base`}>
      <div
        class={tw
          `fixed top-0 left-0 h-16 w-screen text-gray-800 flex items-center px-4 gap-4 border-b-1 border-gray-300 text-lg`}
      >
        <div class={tw`w-56`}>Drive</div>
        <div class={tw`flex-grow`}>
          <input
            placeholder="Search in Drive"
            class={tw`bg-gray-100 px-6 py-3 w-3/5 rounded-md`}
          />
        </div>
        <div class={tw`w-12`}>
          <button>Help</button>
        </div>
        <div class={tw`w-12`}>
          <button>Setting</button>
        </div>
      </div>
      <div class={tw`flex mt-16 w-full pt-4 gap-4`}>
        <div class={tw`w-60 flex flex-col gap-4`}>
          <div>
            <button
              class={tw
                `rounded-full w-32 mx-2 p-3 border-1 shadow-md hover:bg-gray-100`}
            >
              New
            </button>
          </div>
          <div
            class={tw`rounded-r-3xl bg-blue-100 px-4 py-2.5`}
          >
            &gt; <span class={tw`font-bold`}>My Drive</span>
          </div>
        </div>
        <div class={tw`w-full flex-1`}>
          <div
            class={tw`flex-grow border-b-1 border-gray-300 pb-3 px-4 text-lg`}
          >
            My Drive
          </div>
          <div class={tw`pt-2`}>
            <table class={tw`w-11/12 table-auto`}>
              <thead class={tw`border-b-1 text-gray-600 text-left`}>
                <tr>
                  <th class={tw`p-2`}>Name</th>
                  <th class={tw`p-2 w-40`}>Owner</th>
                  <th class={tw`p-2 w-40`}>Last Modified</th>
                  <th class={tw`p-2 w-40`}>File Size</th>
                </tr>
              </thead>
              <tbody>
                <tr class={tw`hover:bg-blue-100`}>
                  <td class={tw`px-2 py-4 font-bold text-gray-600`}>test.md</td>
                  <td class={tw`px-2`}>me</td>
                  <td class={tw`px-2`}>Oct 1, 2020 me</td>
                  <td class={tw`px-2`}>102 KB</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}
