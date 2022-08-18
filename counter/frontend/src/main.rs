use gloo::storage::LocalStorage;
use gloo::storage::Storage;
use yew::prelude::*;

fn main() {
    yew::start_app::<App>();
}

#[function_component(App)]
pub fn app() -> Html {
    let start_value = LocalStorage::get::<i32>("counter").unwrap_or(0);

    html! {
        <Counter {start_value} />
    }
}

#[derive(Properties, PartialEq)]
pub struct CounterProps {
    start_value: i32,
}

#[function_component(Counter)]
pub fn counter(props: &CounterProps) -> Html {
    let counter = use_state(|| props.start_value);
    let onclick = {
        let counter = counter.clone();
        Callback::from(move |_| {
            let new_value = *counter + 1;
            LocalStorage::set::<i32>("counter", new_value).expect("Failed to set counter");
            counter.set(new_value);
        })
    };

    html! {
        <div>
            <button {onclick}>{ "+1" }</button>
            <p>{ *counter }</p>
        </div>
    }
}
